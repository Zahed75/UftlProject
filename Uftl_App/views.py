from django.core import paginator
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
from App_Login.models import *
from Uftl_App.models import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import uuid
import random
import string

# Create your views here.
from Uftl_App.models import Assets, Contact_Assets


def generate_order_id():
    s = 6
    global order_id
    order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=s))
    order_id = "#UF" + str(order_id)
    return order_id
    print(generate_order_id(), "auvee")


def index(request):
    dict = {}

    return render(request, 'Uftl_App/index.html', context=dict)


@login_required()
def assets_contact(request):
    ct_profile = Contact_Assets.objects.filter(user=request.user)
    ft = fuel_utils.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        company_name = request.POST.get('company_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        area = request.POST.get('area')
        contact_photo = request.FILES['contact_photo']
        city = request.POST.get('city')
        billing_add = request.POST.get('billing_add')

        contact_ins = Contact_Assets(
            user=request.user,
            full_name=full_name,
            company_name=company_name,
            phone_number=phone_number,
            email=email,
            area=area,
            contact_photo=contact_photo,
            city=city,
            billing_add=billing_add

        )
        contact_ins.save()
        return redirect('/assets/')
        print(contact_photo)

    dict = {'ft': ft, 'ct_profile': ct_profile}

    return render(request, 'Uftl_App/contactprofile.html', context=dict)


@login_required()
def assets_profile(request):
    ft = fuel_utils.objects.all()
    assets_info = Assets.objects.filter(user=request.user)
    if request.method == 'POST':
        asset_name = request.POST.get('asset_name')
        asset_type = request.POST.get('asset_type')
        fuel_type = request.POST.get('fuel_type')
        asset_location = request.POST.get('asset_location')
        asset_photo = request.FILES['asset_photo']

        print(asset_photo)

        assets_ins = Assets(
            user=request.user,
            asset_name=asset_name,
            asset_type=asset_type,
            fuel_type=fuel_type,
            asset_location=asset_location,
            asset_photo=asset_photo
        )
        assets_ins.save()
        return redirect('/dashboard/')

    dict = {'ft': ft, 'assets_info': assets_info}
    print(assets_info)

    return render(request, 'Uftl_App/assetprofile.html', context=dict)


@login_required()
def Dashboard(request):
    dict = {}
    return render(request, 'Uftl_App/dashboard.html', context=dict)


@login_required()
def order_fuel(request):
    ct_profile = Contact_Assets.objects.filter(user=request.user)
    if request.method == "GET":
        pass

    cp = cupon_code.objects.all()
    oil_price = Fuel_price.objects.all()
    ai = Assets.objects.all()
    ft_utils = fuel_utils.objects.all()
    from django.db.models import Q
    date_time = OrderDashboard.objects.all()
    # test=Fuel_price.objects.filter().last().fuel_ammount
    # test1=Fuel_price.objects.filter().last().total_ammount
    # print("hello",test)
    # print("hello",test1)

    reservation = False
    if request.method == "POST":
        order_id = generate_order_id()
        print(order_id)
        time = request.POST.get('time')
        date = request.POST.get('date')
        fuel_amount = request.POST.get('fuel_amount')
        base_cost = request.POST.get('base_cost')
        discount = request.POST.get('discount')
        total_amount = request.POST.get('total_amount')
        payment_method = request.POST.get('payment_method')
        asset_name = request.POST.get('asset_name')
        fuel_type = request.POST.get('fuel_type')
        reserved = Reserved.objects.filter(Q(time=time) & Q(date=date))
        order_limits = orderlimit.objects.all().last().limit

        print(order_id)

        print(order_limits)

        if reserved.count() >= order_limits:

            reservation = True

            print(reservation)
            # return HttpResponse('Time already reserved!')
            messages.error(request, "This time is already reserved")

        else:
            reserved_ins = Reserved(
                time=time,
                date=date,

            )
            invoice_ins = OrderList(
                user=request.user,
                time=time,
                date=date,
                fuel_amount=fuel_amount,
                base_cost=base_cost,
                discount=discount,
                total_amount=total_amount,
                payment_method=payment_method,
                order_id=order_id,
                asset_name=asset_name,
                fuel_type=fuel_type,

            )
            print(asset_name)

            invoice_ins.save()
            reserved_ins.save()

            messages.success(request, "Your Order Has been placed")
            return redirect('/order_fuel/')

    dict = {'date_time': date_time, 'reservation': reservation, 'ft_utils': ft_utils, 'cp': cp,
            'oil_price': oil_price, 'ai': ai, 'ct_profile': ct_profile}

    return render(request, 'Uftl_App/orderfuel.html', context=dict)


def success_profile(request):
    dict = {}
    return render(request, 'Uftl_App/profile_congo.html', context=dict)


@login_required()
def allassets(request):
    ct_profile = Contact_Assets.objects.filter(user=request.user)
    asset_list = Assets.objects.filter(user=request.user)
    dict = {
        'ct_profile': ct_profile,
        'asset_list': asset_list

    }

    return render(request, 'Uftl_App/allassets.html', context=dict)


@login_required()
def add_assets(request):
    ft_utils = fuel_utils.objects.all()
    if request.method == 'POST':
        asset_name = request.POST.get('asset_name')
        asset_type = request.POST.get('asset_type')
        fuel_type = request.POST.get('fuel_type')
        asset_location = request.POST.get('asset_location')
        asset_photo = request.FILES['asset_photo']

        asset_ins = Assets(
            user=request.user,
            asset_name=asset_name,
            asset_type=asset_type,
            fuel_type=fuel_type,
            asset_location=asset_location,
            asset_photo=asset_photo
        )

        asset_ins.save()
        print("test", asset_ins.asset_photo)
    dict = {
        'ft_utils': ft_utils
    }

    return render(request, 'Uftl_App/addnewasset.html', context=dict)


@login_required()
def edit_assets(request, id):
    all_assets = Assets.objects.get(pk=id)
    # all_assets.asset_name = "hello"
    ct_profile = Contact_Assets.objects.filter(user=request.user)
    # ft_utils = fuel_utils.objects.get(pk=id)
    ft_utils = fuel_utils.objects.all()

    if request.method == 'POST':
        all_assets.asset_name = request.POST.get('asset_name')
        all_assets.asset_type = request.POST.get('asset_type')
        all_assets.asset_location = request.POST.get('asset_location')
        all_assets.fuel_type = request.POST.get('fuel_type')
        all_assets.asset_photo = request.FILES['asset_photo']

    all_assets.save()

    print(all_assets)

    dict = {
        'all_assets': all_assets,
        'ct_profile': ct_profile,
        'ft_utils': ft_utils,
    }

    return render(request, 'Uftl_App/editasset.html', context=dict)


@login_required()
def delete_asset(request, id):
    if request.method == 'GET':
        pi = Assets.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse('uftl.assets_list'))

@login_required()
def report(request):
    
    user_order = OrderList.objects.filter(user=request.user).order_by('id')
    paginator=Paginator(user_order,5) #pagination start
    page_number=request.GET.get('page')
    
    page_obj=paginator.get_page(page_number)
    ct_profile = Contact_Assets.objects.filter(user=request.user)
    at = Assets.objects.filter(user=request.user)

    # if request.method == "POST":
    #     fromdate = request.POST.get['fromdate']
    #     todate = request.POST.get['todate']
    #     displaydata = page_obj.objects.raw('select order_id,asset_name,fuel_amount,total_amount,joindate from employee where joindate between "'+fromdate+'" and "'+todate+'"')
    #     render(request, 'Uftl_App/reporting.html', {'data': displaydata})    
    #     rd = OrderList.objects.filter(Q(report_date__gte = fd) & Q(report_date__lte=td))


    dict = {'user_order': user_order,
            'ct_profile': ct_profile,
            'at': at,
            'page_obj':page_obj
            }

    # print(user_order)
    # print(page_obj)


    return render(request, 'Uftl_App/reporting.html', context=dict)


@login_required()
def edit_profile(request):
    my_profile = Contact_Assets.objects.get(user=request.user)
    my_ft = fuel_utils.objects.all()
    if request.method == 'POST':
        my_profile.full_name = request.POST.get('full_name')
        my_profile.company_name = request.POST.get('company_name')
        my_profile.phone_number = request.POST.get('phone_number')
        my_profile.email = request.POST.get('email')
        my_profile.area = request.POST.get('area')
        # my_profile.contact_photo = request.FILES['contact_photo']
        my_profile.city = request.POST.get('city')
        my_profile.billing_add = request.POST.get('billing_add')
    my_profile.save()

    print(my_profile)
    print(my_profile.area)

    dict = {
        'my_profile': my_profile,
        'my_ft': my_ft,
    }

    # messages.success(request, "Your account has been updated successfully")
    return render(request, 'Uftl_App/editprofile.html', context=dict)

data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('Uftl_App/reporting.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


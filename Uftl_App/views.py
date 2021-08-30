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
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
from App_Login.models import *
from Uftl_App.models import *
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
                fuel_type=fuel_type

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


def allassets(request):
    ct_profile = Contact_Assets.objects.filter(user=request.user)
    asset_list = Assets.objects.filter(user=request.user)
    dict = {
        'ct_profile': ct_profile,
        'asset_list': asset_list

    }

    return render(request, 'Uftl_App/allassets.html', context=dict)


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


def edit_assets(request):
    all_assets = Assets.objects.filter(user=request.user)
    ct_profile = Contact_Assets.objects.all()
    dict = {
        'all_assets': all_assets,
        'ct_profile': ct_profile
    }

    return render(request, 'Uftl_App/editasset.html', context=dict)

def delete_asset(request, id):
    if request.method == 'POST':
        pi = Assets.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/Uftl_App/allassets.html')


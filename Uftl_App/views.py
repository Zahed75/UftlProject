from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
from App_Login.models import *
from Uftl_App.models import *

# Create your views here.
from Uftl_App.models import Assets, Contact_Assets


def index(request):
    dict = {}

    return render(request, 'Uftl_App/index.html', context=dict)


@login_required()
def assets_profile(request):
    ft = fuel_utils.objects.all()
    if request.method == 'POST':
        asset_name = request.POST.get('asset_name')
        asset_type = request.POST.get('asset_type')
        fuel_type = request.POST.get('fuel_type')
        asset_location = request.POST.get('asset_location')
        asset_photo = request.POST.get('asset_photo')
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
        return redirect('/contactprofile/')

    dict = {'ft': ft}

    return render(request, 'Uftl_App/assetprofile.html', context=dict)


@login_required()
def assets_contact(request):
    ft = fuel_utils.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        company_name = request.POST.get('company_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        area = request.POST.get('area')
        contact_photo = request.POST.get('contact_photo')
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
        return redirect('/dashboard/')

    dict = {'ft': ft}

    return render(request, 'Uftl_App/contactprofile.html', context=dict)


@login_required()
def Dashboard(request):
    dict = {}
    return render(request, 'Uftl_App/dashboard.html', context=dict)


@login_required()
def order_fuel(request):
    cp = cupon_code.objects.all()
    oil_price = Fuel_price.objects.all()
    ft_utils = fuel_utils.objects.all()
    from django.db.models import Q
    date_time = OrderDashboard.objects.all()
    # test=Fuel_price.objects.filter().last().fuel_ammount
    # test1=Fuel_price.objects.filter().last().total_ammount
    # print("hello",test)
    # print("hello",test1)

    reservation = False
    if request.method == "POST":
        time = request.POST.get('time')
        date = request.POST.get('date')
        fuel_amount = request.POST.get('fuel_amount')
        base_cost = request.POST.get('base_cost')
        discount = request.POST.get('discount')
        total_amount = request.POST.get('total_amount')
        payment_method = request.POST.get('payment_method')
        reserved = Reserved.objects.filter(Q(time=time) & Q(date=date))
        order_limits = orderlimit.objects.all().last().limit
        print(order_limits)
        if reserved.count() >= order_limits:

            reservation = True

            print(reservation)
            return HttpResponse('Time already reserved!')

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
                payment_method=payment_method
                
            )
            invoice_ins.save()
            reserved_ins.save()

            return HttpResponse('Order confirmed')
    dict = {'date_time': date_time, 'reservation': reservation, 'ft_utils': ft_utils, 'cp': cp,
            'oil_price': oil_price}

    return render(request, 'Uftl_App/orderfuel.html', context=dict)


def success_profile(request):
    dict = {}
    return render(request, 'Uftl_App/profile_congo.html', context=dict)

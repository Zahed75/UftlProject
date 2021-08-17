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
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        company_name=request.POST.get('company_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        area=request.POST.get('area')
        contact_photo=request.POST.get('contact_photo')
        city=request.POST.get('city')
        billing_add=request.POST.get('billing_add')

        contact_ins=Contact_Assets(
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
        return redirect('/order_fuel/')


    dict = {'ft': ft}

    return render(request, 'Uftl_App/contactprofile.html', context=dict)


def order_fuel(request):
    dict={}

    return render(request,'Uftl_App/orderfuel.html',context=dict)

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
from App_Login.models import OrderFuel, Profile, fuel_utils


# Create your views here.

def non_register(request):
    test = OrderFuel.objects.all()
    fuel_des_area = fuel_utils.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        company_name = request.POST.get('company_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        fuel_type = request.POST.get('fuel_type')
        fuel_amount=request.POST.get('fuel_amount')
        order_area = request.POST.get('order_area')
        message = request.POST.get('message')

        order_ins = OrderFuel(full_name=full_name, company_name=company_name,
                              phone_number=phone_number, email=email, fuel_type=fuel_type, order_area=order_area,
                              message=message,fuel_amount=fuel_amount)


        order_ins.save()


    dict = {'test': test, 'fuel_des_area': fuel_des_area}

    return render(request, 'App_Login/form.html', context=dict)


def login(request):
    test = Profile.objects.all()
    print(test)
    dict = {'test': test}

    return render(request, 'App_Login/Login.html', context=dict)


def SignUp(request):
    dict = {}

    return render(request, 'App_Login/signup.html', context=dict)


def success(request):
    dict = {}

    return render(request, 'App_Login/success.html', context=dict)

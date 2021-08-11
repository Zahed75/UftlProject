from django.shortcuts import render,HttpResponse,HttpResponseRedirect
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
from App_Login.models import *
# Create your views here.


def index(request):
    dict={}

    return render(request,'Uftl_App/index.html',context=dict)


def assets(request):

    ft_util = fuel_utils.objects.all()

    dict={"ft_util":ft_util}

    return render(request,'Uftl_App/asset.html',context=dict)

def contact_page(request):
    dict={}

    return render(request,'Uftl_App/contact.html',context=dict)
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
from App_Login.models import *


# Create your views here.


def index(request):
    dict = {}

    return render(request, 'Uftl_App/index.html', context=dict)

@login_required()
def assets_profile(request):
    dict = {}

    return render(request, 'Uftl_App/assetprofile.html', context=dict)

@login_required()
def assets_contact(request):
    dict = {}

    return render(request, 'Uftl_App/contactprofile.html', context=dict)

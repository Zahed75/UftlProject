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
from Driver_App.models import *
from Driver_App.models import *
# Create your views here.

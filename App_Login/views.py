from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from App_Login.models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.views.generic.edit import DeleteView
from django.views import View
from App_Login.models import *
from django.contrib import messages
import uuid
import random
import string


# Create your views here.

def generate_captcha():
    s = 4  # number of characters in the string.
    global captcha
    captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=s))
    captcha = str(captcha)

    return captcha


def non_register(request):
    # captcha start

    if request.method == "GET":
        captcha_run = generate_captcha()
        print(captcha_run)
        print(captcha)

    test = OrderFuel.objects.all()
    fuel_des_area = fuel_utils.objects.all()

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        company_name = request.POST.get('company_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        fuel_type = request.POST.get('fuel_type')
        fuel_amount = request.POST.get('fuel_amount')
        order_area = request.POST.get('order_area')
        message = request.POST.get('message')

        captcha_input = request.POST.get('captcha_input')
        # captcha_input = int(captcha_input)

        print(captcha_input)

        # print(type(captcha))
        # print(type(captcha_input))

        print(captcha)

        if captcha_input == captcha:
            order_ins = OrderFuel(full_name=full_name, company_name=company_name,
                                  phone_number=phone_number, email=email, fuel_type=fuel_type, order_area=order_area,
                                  message=message, fuel_amount=fuel_amount)
            order_ins.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('/')

        else:
            messages.error(request, 'Your captcha in not valid')

    dict = {'test': test, 'fuel_des_area': fuel_des_area, 'captcha': captcha}

    return render(request, 'App_Login/form.html', context=dict)


def Sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')

        login(request, user)
        return redirect('/submitted')

    dict = {}

    return render(request, 'App_Login/Login.html', context=dict)


def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/SignUp')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/SignUp')

            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)
    dict = {}

    return render(request, 'App_Login/signup.html', context=dict)


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/Sign_in')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/Sign_in')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')


def token_send(request):
    dict = {}

    return render(request, 'App_Login/token_send.html', context=dict)


def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi click the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def error_page(request):
    dict = {}

    return render(request, 'App_Login/error.html', context=dict)


def success(request):
    dict = {}

    return render(request, 'App_Login/success.html', context=dict)


def submitted(request):
    dict = {}

    return render(request, 'App_Login/submitted.html', context=dict)



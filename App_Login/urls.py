from django.conf.urls import url
from django.urls import path
from App_Login import views

# app_name = 'App_Login'

urlpatterns = [
    path('Sign_in/', views.Sign_in, name='Sign_in'),
    path('Signup/', views.SignUp, name='Signup'),
    path('token/', views.token_send, name="token_send"),
    path('success/', views.success, name='success'),
    path('verify/<auth_token>/', views.verify, name="verify"),
    path('error/', views.error_page, name="error"),
    path('fuel_order/', views.non_register, name='fuel_order'),
    path('submitted/', views.submitted, name='submitted'),
    path('success/', views.success, name='success'),
    path('forget-password/', views.ForgetPassword, name="forget_password"),
    path('change-password/<token>/', views.ChangePassword, name="change_password"),

]

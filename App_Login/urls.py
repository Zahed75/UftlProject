from django.conf.urls import url
from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [
    path('Login/',views.login,name='Login'),
    path('Signup/',views.SignUp,name='Signup'),
    path('order_fuel/',views.non_register,name='order_fuel'),

]

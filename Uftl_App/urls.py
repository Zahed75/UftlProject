from django.conf.urls import url
from django.urls import path
from Uftl_App import views

app_name = 'Uftl_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/',views.assets_profile,name='asset'),
    path('contactprofile/',views.assets_contact,name='contactprofile'),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('order_fuel/',views.order_fuel,name='order_fuel'),
]

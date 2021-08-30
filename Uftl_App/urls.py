from django.conf.urls import url
from django.urls import path
from Uftl_App import views

# app_name = 'Uftl_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.assets_profile, name='asset'),
    path('contactprofile/', views.assets_contact, name='contactprofile'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('order_fuel/', views.order_fuel, name='order_fuel'),
    path('profile_done/',views.success_profile,name='profile_done'),
    path('assets_list/',views.allassets,name='uftl.assets_list'),
    path('add_assets/',views.add_assets,name='add_assets'),
    path('edit_assets/',views.edit_assets,name='edit_assets'),
    path('delete/<int:id>/', views.delete_asset, name='deleteasset'),

]

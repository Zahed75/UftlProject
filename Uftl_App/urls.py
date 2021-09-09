from django.conf.urls import url
from django.urls import path
from Uftl_App import views

# app_name = 'Uftl_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.assets_profile, name='asset'),
    path('contactprofile/', views.assets_contact, name='contactprofile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('order_fuel/', views.order_fuel, name='order_fuel'),
    path('profile_done/',views.success_profile,name='profile_done'),

    path('assets_list/',views.allassets,name='uftl.assets_list'),
    path('add_assets/',views.add_assets,name='add_assets'),
    path('edit_assets/<int:id>',views.edit_assets,name='edit_assets'),
    path('delete/<int:id>/', views.delete_asset, name='deleteasset'),
    path('user-report/',views.report,name='report'),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]

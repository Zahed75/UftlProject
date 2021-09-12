from django.conf.urls import url
from django.urls import path
from Uftl_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.assets_profile, name='asset'),
    path('contactprofile/', views.assets_contact, name='contactprofile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('order_fuel/', views.order_fuel, name='order_fuel'),
    path('profile_done/', views.success_profile, name='profile_done'),
    path('assets_list/', views.allassets, name='uftl.assets_list'),
    path('add_assets/', views.add_assets, name='add_assets'),
    path('edit_assets/<int:id>', views.edit_assets, name='edit_assets'),
    path('delete/<int:id>/', views.delete_asset, name='deleteasset'),
    path('user-report/', views.report, name='report'),
    path('details_order/<int:pk>/', views.order_details, name='order_details'),
    path('pdf/', views.render_pdf_view, name='test-view'),
    path('excel/', views.export_users_xls, name='export_excel'),
    path('driver_dashboard/', views.driver_dashboard, name='driver_dashboard'),

]

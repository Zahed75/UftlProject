from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Assets)
class AssetsAdmin(admin.ModelAdmin):
    list_display = ('user', 'asset_name', 'asset_type', 'asset_location')


@admin.register(Contact_Assets)
class Contact_AssetsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company_name', 'phone_number', 'area')


@admin.register(OrderDashboard)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'reserved']


@admin.register(Reserved)
class ReservedAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'date']


@admin.register(orderlimit)
class orderlimitAdmin(admin.ModelAdmin):
    list_display = ('limit','id')

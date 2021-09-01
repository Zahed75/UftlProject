from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Assets)
class AssetsAdmin(admin.ModelAdmin):
    list_display = ('user', 'asset_name', 'asset_type', 'asset_location', 'fuel_type')


@admin.register(Contact_Assets)
class Contact_AssetsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company_name', 'phone_number', 'area')


@admin.register(OrderDashboard)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'reserved', ]


@admin.register(Reserved)
class ReservedAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'date']


@admin.register(orderlimit)
class orderlimitAdmin(admin.ModelAdmin):
    list_display = ('limit', 'id')


@admin.register(cupon_code)
class cupon_codeAdmin(admin.ModelAdmin):
    list_display = ('id', 'promo_code', 'discount')


@admin.register(Fuel_price)
class Fuel_priceAdmin(admin.ModelAdmin):
    list_display = ('id', 'disel_price', 'octen_price', 'delivery_charge', 'total_amount', 'fuel_amount')


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'date', 'fuel_amount', 'fuel_type', 'asset_name', 'base_cost', 'total_amount', 'discount', 'payment_method','order_id')

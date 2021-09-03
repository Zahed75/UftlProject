from django.contrib import admin
from .models import *


# Register your models here.

# admin.site.register(OrderFuel)
# admin.site.register(Profile)
# admin.site.register(fuel_utils)

@admin.register(OrderFuel)
class OrderFuelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number','fuel_amount','company_name','order_area')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user','created_at')

@admin.register(fuel_utils)
class fuel_utilsAdmin(admin.ModelAdmin):
    list_display = ('fuel_type', 'order_area','asset_type','city')
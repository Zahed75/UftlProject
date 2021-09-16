from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Assets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=220, blank=False)
    asset_type = models.CharField(max_length=220, blank=False)
    fuel_type = models.CharField(max_length=220)
    asset_location = models.TextField(max_length=400, blank=False)
    asset_photo = models.ImageField(upload_to='gallery', blank=False)


class Contact_Assets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=220)
    company_name = models.CharField(max_length=220, blank=True)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=220, blank=True)
    area = models.CharField(max_length=220)
    contact_photo = models.ImageField(upload_to='contact_files')
    city = models.CharField(max_length=300)
    billing_add = models.CharField(max_length=300)



class OrderDashboard(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(verbose_name='Please put your time', blank=True)
    reserved = models.BooleanField(default=False)


class Reserved(models.Model):
    time = models.TimeField(blank=True)
    date = models.DateField(blank=True)


class orderlimit(models.Model):
    limit = models.IntegerField(default='1')


class cupon_code(models.Model):
    promo_code = models.CharField(max_length=40, blank=True)
    discount = models.IntegerField(default='1')


class Fuel_price(models.Model):
    fuel_amount = models.IntegerField(default='1')
    base_cost = models.IntegerField(default='1')
    disel_price = models.IntegerField(default='1', null=True)
    octen_price = models.IntegerField(default='1', null=True)
    total_amount = models.IntegerField(default='1', null=True)
    delivery_charge = models.IntegerField(default='1', null=True)


class OrderList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    time = models.TimeField(blank=True)
    date = models.DateField(blank=True)
    asset_name = models.CharField(max_length=300, blank=True)
    asset_location = models.CharField(max_length=300, blank=True)
    fuel_type = models.CharField(max_length=300, blank=True)
    fuel_amount = models.IntegerField(default='1')
    base_cost = models.IntegerField(default='1')
    discount = models.IntegerField(default='1')
    order_id = models.CharField(max_length=20, blank=True)
    total_amount = models.IntegerField(default='1')
    payment_method = models.CharField(max_length=300, blank=True)

    # STATUS = (
    #     ('PROCESSING', 'PROCESSING'),
    #     ('ON THE WAY', 'ON THE WAY'),
    #     ('DELIVERED', 'DELIVERED'),
    # )

    STATUS = (
        (1, 'PROCESSING'),
        (2, 'ON THE WAY'),
        (3, 'DELIVERED'),
    )

    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0])
    driver_status = models.CharField(max_length=30, default="Processing")



# class driver_dashboard(models.Model):
#     driver_name=models.CharField(max_length=220,blank=True)
#     order_info=models.ForeignKey(OrderList,on_delete=models.CASCADE,related_name='driver_data')
#     date=models.DateField(auto_now_add=True)

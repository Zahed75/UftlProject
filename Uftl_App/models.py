from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Assets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=220, blank=False)
    asset_type = models.CharField(max_length=220, blank=False)
    fuel_type = models.CharField(max_length=220)
    asset_location = models.TextField(max_length=400, blank=False)
    asset_photo = models.FileField(upload_to='Asset')


class Contact_Assets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=220)
    company_name = models.CharField(max_length=220, blank=True)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=220, blank=True)
    area = models.CharField(max_length=220)
    contact_photo = models.FileField(upload_to='contact_files')
    city = models.CharField(max_length=300)
    billing_add = models.CharField(max_length=300)


class OrderDashboard(models.Model):
    time = models.TimeField()
    reserved = models.BooleanField(default=False)

class Reserved(models.Model):
    time = models.TimeField()
    date = models.DateField()

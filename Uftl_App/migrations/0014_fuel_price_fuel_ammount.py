# Generated by Django 3.2.6 on 2021-08-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uftl_App', '0013_rename_price_fuel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_price',
            name='fuel_ammount',
            field=models.IntegerField(default='1', max_length=100),
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0010_auto_20210816_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_utils',
            name='city',
            field=models.CharField(blank=True, max_length=220),
        ),
    ]

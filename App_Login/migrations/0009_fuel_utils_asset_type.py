# Generated by Django 3.2.6 on 2021-08-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0008_auto_20210812_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_utils',
            name='asset_type',
            field=models.CharField(default=1, max_length=220),
            preserve_default=False,
        ),
    ]

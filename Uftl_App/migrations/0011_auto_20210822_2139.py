# Generated by Django 3.2.6 on 2021-08-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uftl_App', '0010_auto_20210822_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='cupon_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_code', models.CharField(blank=True, max_length=40)),
                ('discount', models.IntegerField(default='1')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdashboard',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='orderdashboard',
            name='promo_code',
        ),
    ]
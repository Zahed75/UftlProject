# Generated by Django 3.2.6 on 2021-08-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uftl_App', '0009_alter_orderdashboard_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserved',
            name='limit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

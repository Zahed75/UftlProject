# Generated by Django 3.2.6 on 2021-08-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uftl_App', '0002_auto_20210811_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='asset_type',
            field=models.CharField(max_length=120, null=True),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uftl_App', '0027_alter_assets_asset_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='asset_photo',
            field=models.FileField(upload_to='gallery'),
        ),
    ]
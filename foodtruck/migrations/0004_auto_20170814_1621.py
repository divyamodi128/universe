# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-14 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0003_auto_20170808_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='image',
            field=models.ImageField(blank=True, default='/media/Truck-Images/Default.jpg', null=True, upload_to='Truck-Images'),
        ),
    ]

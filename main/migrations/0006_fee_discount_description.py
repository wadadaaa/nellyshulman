# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_fee_increase_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='discount_description',
            field=models.TextField(blank=True, help_text='Discount Description'),
        ),
    ]

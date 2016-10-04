# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161004_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benefit',
            name='image',
        ),
        migrations.AddField(
            model_name='benefit',
            name='icon',
            field=models.CharField(blank=True, help_text='Benegit icon from fontawesome', max_length=80),
        ),
    ]

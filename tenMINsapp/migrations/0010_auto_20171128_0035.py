# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenMINsapp', '0009_auto_20171127_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='all_choice',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='new_choice',
            field=models.BooleanField(default=False),
        ),
    ]
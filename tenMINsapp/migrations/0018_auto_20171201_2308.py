# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenMINsapp', '0017_auto_20171201_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='sex',
            new_name='user_sex',
        ),
    ]

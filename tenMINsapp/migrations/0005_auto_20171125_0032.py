# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenMINsapp', '0004_auto_20171125_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 02:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenMINsapp', '0005_auto_20171125_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]

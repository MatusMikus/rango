# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 15:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170126_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='views',
            new_name='cViews',
        ),
    ]

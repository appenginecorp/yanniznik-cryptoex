# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-20 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
    ]
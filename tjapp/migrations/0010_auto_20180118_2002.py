# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tjapp', '0009_auto_20171203_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
    ]
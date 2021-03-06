# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tjapp', '0006_auto_20171203_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='CustomerServicePhone',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='company',
            name='WebUrlContactUs',
            field=models.URLField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='route',
            name='Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]

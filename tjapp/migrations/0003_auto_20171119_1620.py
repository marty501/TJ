# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tjapp', '0002_auto_20171119_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='CustomerServicePhone',
            field=models.URLField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='WebUrl',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='WebUrlContactUs',
            field=models.URLField(max_length=250, null=True),
        ),
    ]
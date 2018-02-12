# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 19:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tjapp', '0007_auto_20171203_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DelayAtDepartureStationMins', models.PositiveSmallIntegerField()),
                ('IsCancelled', models.BooleanField()),
                ('ScheduledDepartureTime', models.TimeField()),
                ('ActualArrivalTime', models.TimeField(blank=True)),
                ('Notes', models.CharField(blank=True, default='', max_length=250)),
                ('IsVerified', models.BooleanField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('ArrivalStation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='journey_station_arr', to='tjapp.Station')),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_journeys', to='tjapp.Company')),
                ('DepartureStation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='journey_station_dep', to='tjapp.Station')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_journey', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='route',
            name='ArrivalStation',
        ),
        migrations.RemoveField(
            model_name='route',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='route',
            name='DepartureStation',
        ),
        migrations.RemoveField(
            model_name='routestatus',
            name='Route',
        ),
        migrations.RemoveField(
            model_name='routestatus',
            name='Station',
        ),
        migrations.RemoveField(
            model_name='routestatus',
            name='User',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='RouteStatus',
        ),
    ]
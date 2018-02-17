# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-17 13:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20180214_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='survey_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 22, 13, 12, 20, 766897, tzinfo=utc), verbose_name='опрос с'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30, verbose_name='город'),
        ),
    ]

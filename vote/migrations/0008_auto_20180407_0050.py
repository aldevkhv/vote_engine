# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-06 14:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0007_auto_20180407_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='survey_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 14, 50, 8, 205069, tzinfo=utc), verbose_name='голосование с'),
        ),
    ]

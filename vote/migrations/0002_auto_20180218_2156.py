# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-18 11:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='survey_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 23, 11, 56, 3, 558585, tzinfo=utc), verbose_name='опрос с'),
        ),
    ]
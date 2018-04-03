# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-02 23:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20180403_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participate',
            old_name='content',
            new_name='content_file',
        ),
        migrations.AlterField(
            model_name='competition',
            name='survey_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 23, 35, 24, 44666, tzinfo=utc), verbose_name='голосование с'),
        ),
    ]

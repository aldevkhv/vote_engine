# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-04 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20180204_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='Content',
            field=models.FileField(default=1, upload_to='documents/', verbose_name='файл'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-08 03:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('Survey_date', models.DateTimeField(default=datetime.datetime(2018, 2, 13, 3, 39, 45, 54790, tzinfo=utc), verbose_name='опрос с')),
                ('Type', models.IntegerField(choices=[(1, 'Фотоконкурс'), (2, 'Литературный конкурс'), (3, 'Видеоконкурс'), (4, 'Аудиоконкурс')], default=1, verbose_name='тип конкурса')),
                ('Rules', mezzanine.core.fields.RichTextField(max_length=2000, verbose_name='правила')),
                ('Description', models.TextField(max_length=500, verbose_name='краткое описание')),
            ],
            options={
                'verbose_name_plural': 'конкурсы',
                'verbose_name': 'конкурс',
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('Comment', models.TextField(verbose_name='комментарий')),
                ('Content', models.FileField(blank=True, upload_to='documents/', verbose_name='файл')),
                ('competition_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participates_competition', to='vote.Competition', verbose_name='конкурс')),
            ],
            options={
                'verbose_name_plural': 'заявки на конкурс',
                'verbose_name': 'заявка на конкурс',
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls_participate', to='vote.Participate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='poll',
            unique_together=set([('user', 'participate')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0031_auto_20180328_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvnews_video',
            name='srt_extension',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
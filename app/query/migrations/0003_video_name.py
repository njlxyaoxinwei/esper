# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_video_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0020_segment_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='type',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='things',
        ),
        migrations.DeleteModel(
            name='Thing',
        ),
        migrations.DeleteModel(
            name='ThingType',
        ),
    ]
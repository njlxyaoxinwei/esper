# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0010_tvnews_topictrack_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='tvnews_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tvnews_VideoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_index=True, max_length=256)),
                ('num_frames', models.IntegerField()),
                ('fps', models.FloatField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('has_captions', models.BooleanField(default=False)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='videotag', to='query.tvnews_Tag')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='videotag', to='query.tvnews_Video')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

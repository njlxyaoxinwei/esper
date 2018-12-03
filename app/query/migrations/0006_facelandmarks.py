# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0005_auto_20181119_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceLandmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmarks', models.BinaryField()),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Face')),
                ('labeler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
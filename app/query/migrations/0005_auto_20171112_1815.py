# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import query.base_models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0004_auto_20171109_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='babycam_Pose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bbox_x1', models.FloatField()),
                ('bbox_x2', models.FloatField()),
                ('bbox_y1', models.FloatField()),
                ('bbox_y2', models.FloatField()),
                ('bbox_score', models.FloatField()),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='pose', to='query.babycam_Frame')),
                ('labeler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='pose', to='query.babycam_Labeler')),
            ],
            bases=(models.Model, query.base_models.Pose),
        ),
        migrations.CreateModel(
            name='babycam_PoseFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.BinaryField()),
                ('labeler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='posefeatures', to='query.babycam_Labeler')),
                ('pose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='posefeatures', to='query.babycam_Pose')),
            ],
        ),
        migrations.CreateModel(
            name='babycam_PoseTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='tvnews_pose',
            name='keypoints',
        ),
        migrations.RemoveField(
            model_name='tvnews_posetrack',
            name='keypoints',
        ),
        migrations.AddField(
            model_name='babycam_pose',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='pose', to='query.babycam_PoseTrack'),
        ),
        migrations.AlterUniqueTogether(
            name='babycam_posefeatures',
            unique_together=set([('labeler', 'pose')]),
        ),
        migrations.AlterUniqueTogether(
            name='babycam_pose',
            unique_together=set([('track', 'frame', 'labeler')]),
        ),
    ]
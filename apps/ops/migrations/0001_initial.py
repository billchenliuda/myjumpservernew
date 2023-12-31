# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-24 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdHoc',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('_tasks', models.TextField(verbose_name='Tasks')),
                ('pattern', models.CharField(default='{}', max_length=64, verbose_name='Pattern')),
                ('_options', models.CharField(default='', max_length=1024, verbose_name='Options')),
                ('_hosts', models.TextField(blank=True, verbose_name='Hosts')),
                ('run_as_admin', models.BooleanField(default=False, verbose_name='Run as admin')),
                ('run_as', models.CharField(default='', max_length=128, verbose_name='Run as')),
                ('_become', models.CharField(default='', max_length=1024, verbose_name='Become')),
                ('created_by', models.CharField(default='', max_length=64, null=True, verbose_name='Create by')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ops_adhoc',
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='AdHocRunHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name='Start time')),
                ('date_finished', models.DateTimeField(blank=True, null=True, verbose_name='End time')),
                ('timedelta', models.FloatField(default=0.0, null=True, verbose_name='Time')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Is finished')),
                ('is_success', models.BooleanField(default=False, verbose_name='Is success')),
                ('_result', models.TextField(blank=True, null=True, verbose_name='Adhoc raw result')),
                ('_summary', models.TextField(blank=True, null=True, verbose_name='Adhoc result summary')),
                ('adhoc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history', to='ops.AdHoc')),
            ],
            options={
                'db_table': 'ops_adhoc_history',
                'get_latest_by': 'date_start',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('interval', models.IntegerField(blank=True, help_text='Units: seconds', null=True, verbose_name='Interval')),
                ('crontab', models.CharField(blank=True, help_text='5 * * * *', max_length=128, null=True, verbose_name='Crontab')),
                ('is_periodic', models.BooleanField(default=False, verbose_name='Periodic perform')),
                ('callback', models.CharField(blank=True, max_length=128, null=True, verbose_name='Callback')),
                ('is_deleted', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('created_by', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ops_task',
                'get_latest_by': 'date_created',
            },
        ),
        migrations.AddField(
            model_name='adhocrunhistory',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history', to='ops.Task'),
        ),
        migrations.AddField(
            model_name='adhoc',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adhoc', to='ops.Task'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-30 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='createdDate',
        ),
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time'),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-31 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20200201_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='Add Comment'),
        ),
    ]

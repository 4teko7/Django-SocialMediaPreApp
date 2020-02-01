# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-01 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20200201_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=4000, verbose_name='Yorum Ekle'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Olu\u015fturulma Tarihi'),
        ),
    ]
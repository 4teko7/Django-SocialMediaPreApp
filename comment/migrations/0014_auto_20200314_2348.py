# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-14 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0013_comment_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='userImage',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim Ekle/Add Picture'),
        ),
    ]

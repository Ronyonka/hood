# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-24 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20190324_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

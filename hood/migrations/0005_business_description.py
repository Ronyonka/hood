# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-24 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_business_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

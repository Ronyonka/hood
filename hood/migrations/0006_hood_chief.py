# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-25 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_business_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='hood',
            name='chief',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

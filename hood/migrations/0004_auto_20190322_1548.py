# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-22 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20190322_1447'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Neighbourhood',
            new_name='Hood',
        ),
    ]

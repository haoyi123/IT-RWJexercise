# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170125_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]

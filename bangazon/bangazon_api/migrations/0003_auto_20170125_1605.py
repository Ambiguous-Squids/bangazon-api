# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_api', '0002_auto_20170124_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

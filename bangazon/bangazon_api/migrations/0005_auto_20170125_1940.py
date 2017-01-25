# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_api', '0004_paymenttype_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymenttype',
            old_name='name',
            new_name='payment_type_name',
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='category',
            field=models.CharField(default='some string', max_length=50),
        ),
    ]
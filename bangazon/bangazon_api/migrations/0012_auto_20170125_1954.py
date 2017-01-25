# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_api', '0011_auto_20170125_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttype',
            name='payment_type_name',
            field=models.CharField(choices=[('None', 'None'), ('VISA', 'VISA'), ('MasterCard', 'MasterCard'), ('American Express', 'American Express')], default='None', max_length=16),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('account_created', models.DateTimeField(auto_now_add=True)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon_api.Customer')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type_name', models.CharField(choices=[('', ''), ('VISA', 'VISA'), ('MasterCard', 'MasterCard'), ('American Express', 'American Express')], default='', max_length=16)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=16, unique=True)),
                ('expiration_date', models.DateField()),
                ('ccv', models.CharField(max_length=3)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon_api.Customer')),
            ],
            options={
                'verbose_name_plural': 'PaymentTypes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=4000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon_api.Customer')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'ProductTypes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon_api.ProductType'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon_api.PaymentType'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='bangazon_api.Product'),
        ),
    ]

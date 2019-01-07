# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=10)),
                ('father_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')])),
                ('mail_id', models.EmailField(max_length=100, unique=True)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Customer_images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=10)),
                ('father_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')])),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('join_date', models.DateField(auto_now=True)),
                ('experience_in_year', models.IntegerField()),
                ('mail_id', models.EmailField(max_length=100, unique=True)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Employee_images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_desc', models.CharField(max_length=200)),
                ('product_mfg_date', models.DateField(auto_now=True)),
                ('product_exp_date', models.DateField(auto_now=True)),
                ('product_image', models.ImageField(upload_to='product_images', blank=True)),
                ('number_of_products', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='product_type',
            field=models.ForeignKey(to='store.ProductType'),
        ),
    ]

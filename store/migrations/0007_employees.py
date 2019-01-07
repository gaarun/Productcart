# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20180218_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('middele_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.CharField(default='M', max_length=1)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('join_date', models.DateField(auto_now=True)),
                ('experience_in_year', models.IntegerField()),
                ('mail_id', models.EmailField(max_length=100, unique=True)),
                ('mobile_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(default='M', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=2),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(default='M', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=2),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20180220_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]

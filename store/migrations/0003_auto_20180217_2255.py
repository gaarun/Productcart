# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180217_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_exp_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_mfg_date',
            field=models.DateField(),
        ),
    ]

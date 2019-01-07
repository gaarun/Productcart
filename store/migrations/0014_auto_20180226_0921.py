# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20180226_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mail_id',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]

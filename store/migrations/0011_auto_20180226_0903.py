# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20180226_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]

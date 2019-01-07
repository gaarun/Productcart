# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20180226_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mail_id',
            field=models.EmailField(max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20180226_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
    ]

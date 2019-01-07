# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_employees'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employees',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_delete_employees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='experience_in_year',
            new_name='experience',
        ),
    ]

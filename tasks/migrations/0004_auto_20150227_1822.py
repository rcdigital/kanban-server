# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20150226_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='state',
            new_name='status',
        ),
    ]

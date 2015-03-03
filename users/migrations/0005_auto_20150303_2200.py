# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150227_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanbanusers',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data'),
            preserve_default=True,
        ),
    ]

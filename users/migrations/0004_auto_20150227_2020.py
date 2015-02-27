# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150227_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanbanusers',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 27, 20, 20, 41, 884443), verbose_name=b'Data'),
            preserve_default=True,
        ),
    ]

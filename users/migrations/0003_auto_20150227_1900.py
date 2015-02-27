# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150227_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanbanusers',
            name='thumb',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Url Thumb', blank=True),
            preserve_default=True,
        ),
    ]

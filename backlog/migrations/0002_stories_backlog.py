# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='backlog',
            field=models.ForeignKey(verbose_name=b'Backlog', blank=True, to='backlog.Backlogs', null=True),
            preserve_default=True,
        ),
    ]

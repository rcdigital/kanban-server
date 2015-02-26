# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0002_stories_backlog'),
        ('tasks', '0002_auto_20150226_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='backlog',
        ),
        migrations.AddField(
            model_name='tasks',
            name='story',
            field=models.ForeignKey(verbose_name=b'Backlog', blank=True, to='backlog.Stories', null=True),
            preserve_default=True,
        ),
    ]

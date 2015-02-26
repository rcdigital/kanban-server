# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='estimate_time',
            field=models.IntegerField(null=True, verbose_name=b'Estimado', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasks',
            name='finish_time',
            field=models.IntegerField(null=True, verbose_name=b'Tempo Realizado', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasks',
            name='state',
            field=models.CharField(default=b'todo', max_length=255, verbose_name=b'status', choices=[(b'To do', b'todo'), (b'Doing', b'doing'), (b'Done', b'done')]),
            preserve_default=True,
        ),
    ]

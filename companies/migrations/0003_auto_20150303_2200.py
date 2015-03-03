# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_roles_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='owner',
            field=models.ForeignKey(related_name='companies', to='users.KanbanUsers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companies',
            name='thumb',
            field=models.FileField(null=True, upload_to=b'company_thumbs/', blank=True),
            preserve_default=True,
        ),
    ]

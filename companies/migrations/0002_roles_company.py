# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='company',
            field=models.ForeignKey(verbose_name=b'empresa', blank=True, to='companies.Companies', null=True),
            preserve_default=True,
        ),
    ]

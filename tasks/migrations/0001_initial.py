# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('backlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Tarefa')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(verbose_name=b'Data')),
                ('hash_id', models.CharField(default=tasks.models._create_hash, unique=True, max_length=255, verbose_name=b'hash')),
                ('backlog', models.ForeignKey(verbose_name=b'Backlog', to='backlog.Backlogs')),
                ('created_by', models.ForeignKey(verbose_name=b'Criado por', to='companies.Members')),
                ('doing_by', models.ForeignKey(related_name='doing_by', verbose_name=b'Feito por', to='companies.Members')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

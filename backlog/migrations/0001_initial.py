# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import backlog.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Backlog')),
                ('hash_id', models.CharField(default=backlog.models._create_hash, unique=True, max_length=255, verbose_name=b'hash')),
                ('project', models.ForeignKey(verbose_name=b'Projeto', to='projects.Projects')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Estoria')),
                ('order', models.IntegerField(verbose_name=b'Ordem')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(verbose_name=b'Data')),
                ('hash_id', models.CharField(default=backlog.models._create_hash, unique=True, max_length=255, verbose_name=b'hash')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

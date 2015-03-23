# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import users.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KanbanUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('thumb', models.CharField(max_length=255, null=True, verbose_name=b'Url Thumb', blank=True)),
                ('hash_id', models.CharField(default=users.models._create_hash, unique=True, max_length=255, verbose_name=b'hash')),
                ('open_id', models.CharField(max_length=255, null=True, verbose_name=b'open id', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            bases=(models.Model,),
        ),
    ]

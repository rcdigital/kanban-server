# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import companies.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome')),
                ('thumb', models.FileField(upload_to=b'company_thumbs/')),
                ('hash_id', models.CharField(default=companies.models._create_hash, unique=True, max_length=255, verbose_name=b'hash')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to='users.Users')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash_id', models.CharField(default=companies.models._create_hash, unique=True, max_length=255, verbose_name=b'hash')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(verbose_name=b'Empresa', to='companies.Companies')),
                ('member', models.ForeignKey(verbose_name=b'membro', to='users.Users')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Setor')),
                ('color', models.CharField(max_length=255, verbose_name=b'cor')),
                ('hash_id', models.CharField(default=companies.models._create_hash, unique=True, max_length=255, verbose_name=b'hash')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pap\xe9is',
                'verbose_name_plural': 'Pap\xe9is',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='members',
            name='role',
            field=models.ForeignKey(to='companies.Roles'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf8 -*-
from django.db import models
import hashlib
import random
import datetime

from backlog.models import Stories 
from companies.models import Members


def _create_hash():
    return hashlib.sha224(str(random.getrandbits(128))).hexdigest()

TODO = 'To do'
DOING= 'Doing'
DONE = 'Done'
STATUS_CHOICES = (
    ('todo',TODO),
    ('doing', DOING),
    ('done', DONE),
)

class Tasks(models.Model):
    name = models.CharField('Tarefa', max_length=255, null = True, blank = True)
    story = models.ForeignKey(Stories, verbose_name='Backlog', null = True, blank = True)
    estimate_time = models.IntegerField('Estimado', null= True, blank= True)
    finish_time = models.IntegerField('Tempo Realizado', null= True, blank= True)
    status = models.CharField('status', max_length =255, choices=STATUS_CHOICES, default='todo')
    created_by = models.ForeignKey(Members, related_name='created_by', verbose_name='Criado por', null = True, blank = True)
    doing_by = models.ForeignKey(Members, verbose_name='Feito por', related_name="doing_by", null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField('Data', default = datetime.datetime.now)
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)

# -*- coding: utf8 -*-
from django.db import models
import hashlib
import random

from backlog.models import Stories 
from companies.models import Members


def _create_hash():
    return hashlib.sha224(str(random.getrandbits(128))).hexdigest()

TODO = 'To do'
DOING= 'Doing'
DONE = 'Done'
STATUS_CHOICES = (
    (TODO, 'todo'),
    (DOING, 'doing'),
    (DONE, 'done'),
)

class Tasks(models.Model):
    name = models.CharField('Tarefa', max_length=255)
    story = models.ForeignKey(Stories, verbose_name='Backlog', null = True, blank = True)
    estimate_time = models.IntegerField('Estimado', null= True, blank= True)
    finish_time = models.IntegerField('Tempo Realizado', null= True, blank= True)
    status = models.CharField('status', max_length =255, choices=STATUS_CHOICES, default='todo')
    created_by = models.ForeignKey(Members, verbose_name='Criado por')
    doing_by = models.ForeignKey(Members, verbose_name='Feito por', related_name="doing_by")
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField('Data')
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)

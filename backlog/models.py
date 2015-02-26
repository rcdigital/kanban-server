# -*- coding: utf8 -*-
from django.db import models
import hashlib
import random

from projects.models import Projects

def _create_hash():
    return hashlib.sha224(str(random.getrandbits(128))).hexdigest()

class Backlogs(models.Model):
    name = models.CharField('Backlog', max_length= 255)
    project = models.ForeignKey(Projects, verbose_name='Projeto')
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)


class Stories(models.Model):
    name = models.CharField('Estoria', max_length= 255)
    backlog = models.ForeignKey(Backlogs, verbose_name="Backlog", null= True, blank = True)
    order = models.IntegerField('Ordem')
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField('Data')
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)

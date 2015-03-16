# -*- coding: utf8 -*-
from django.db import models
import hashlib
import random
import datetime

from companies.models import Companies

def _create_hash():
    return hashlib.sha224(str(random.getrandbits(128))).hexdigest()

class Projects(models.Model):
    name = models.CharField('Project', max_length= 255)
    company = models.ForeignKey(Companies, verbose_name='Empresa')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField('Data', default = datetime.datetime.now)
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

# -*- coding: utf8 -*-
from django.db import models
import hashlib
import random

from users.models import KanbanUsers
# Create your models here.

def _create_hash():
    return hashlib.sha224(str(random.getrandbits(128))).hexdigest()

class Companies(models.Model):
    name = models.CharField('Nome', max_length=255)
    thumb = models.FileField(upload_to='company_thumbs/', blank=True, null = True)
    owner = models.ForeignKey(KanbanUsers, related_name='companies')
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class Roles (models.Model):
    name = models.CharField('Setor', max_length=255);
    color = models.CharField('cor', max_length=255);
    company = models.ForeignKey(Companies, verbose_name='empresa', blank= True, null = True)
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Papéis'
        verbose_name_plural = 'Papéis'

class Members (models.Model):
    company = models.ForeignKey(Companies, related_name="company", verbose_name='Empresa')
    member = models.ForeignKey(KanbanUsers, related_name="member", verbose_name='membro')
    role = models.ForeignKey(Roles, related_name="role", null= True, blank= True);
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

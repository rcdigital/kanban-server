# -*- coding: utf8 -*-
from django.db import models
import hashlib
import random

def _create_hash():
    return hashlib.sha224(str(random.getrandbits(128))).hexdigest()

class Users(models.Model):
    name = models.CharField('Nome', max_length= 255)
    email = models.EmailField('Email')
    thumb = models.CharField('Url Thumb', max_length= 255)
    hash_id = models.CharField('hash', max_length= 255 ,default = _create_hash, unique = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField('Data')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


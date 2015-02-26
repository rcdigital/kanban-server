import os
PATH = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = '-a+(ijzs_quv2z&$!n@(-n794hl+4e#iwgo)z3#@i!&3$di2&l'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
LANGUAGE_CODE = 'pt-br'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PATH, 'db.sqlite3'),
    }
}

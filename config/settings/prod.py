from .base import *

ALLOWED_HOSTS = ['192.168.137.101']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '192.168.137.101',
        'PORT': '5432',
    }
}
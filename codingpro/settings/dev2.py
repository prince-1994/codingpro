from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'somekeytostartdev2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sbpg',
        'USER': 'postgres',
        'PASSWORD' : 'pass123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
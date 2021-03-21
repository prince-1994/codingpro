from .base import *
import environ

env = environ.Env()

# reading .env file
environ.Env.read_env('.prod.env')


SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(":")

SQLITE_DB_NAME = env('SQLITE_DB_NAME')

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': env('DB_NAME'),
    #     'USER': env('DB_USER'),
    #     'PASSWORD' : env('DB_PASS'),
    #     'HOST': env('DB_HOST'),
    #     'PORT': env('DB_PORT'),
    # }

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR / SQLITE_DB_NAME,
    }
}

CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SECURE = False

SECURE_HSTS_SECONDS = None

SECURE_HSTS_INCLUDE_SUBDOMAINS = False

SECURE_HSTS_PRELOAD = False

SECURE_SSL_REDIRECT = False

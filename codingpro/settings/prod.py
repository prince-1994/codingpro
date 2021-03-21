from .base import *
import environ

env = environ.Env()

# reading .env file
environ.Env.read_env('.prod.env')


SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(":")

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
        'NAME': PROJECT_DIR / 'prod.db.sqlite3',
    }
}

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True
from .base import *
import config.db as db
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['devcenter.heroku.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'deaefe7cdvrohv',
        'USER': 'puvivbqxsyuzgw',
        'PASSWORD': '387152efef718090bdd168d6d0a0ce9ac0fcc72c495fbadbe1c1255d7583d26c',
        'HOST': 'ec2-52-22-216-69.compute-1.amazonaws.com',
        'PORT': 5432,
        'OPTIONS': {
            'options': '-c search_path=prueba'
        },
    }
}

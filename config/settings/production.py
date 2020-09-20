from .base import *
import config.db as db
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['devcenter.heroku.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = db.SQLITE

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


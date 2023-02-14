from .base import *

SECRET_KEY='django-insecure-21m3eo$rybdt1hy#s_*lszn-xz*kz%$2sb^8nr+izjy_h1e$z6'

DEBUG = True

ALLOWED_HOSTS = ['*']

# INSTALLED_APPS += ['debug_toolbar']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
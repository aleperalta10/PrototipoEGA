from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ega',
        'USER' : 'ega',
        'PASSWORD' : 'sistemaega',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'
MEDIA_URL = 'http://localhost:8000/media/'
MEDIA_ROOT = BASE_DIR.child('media')

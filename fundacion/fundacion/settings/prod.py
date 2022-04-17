from tkinter import TRUE
from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = ['https://fundacioncristoredentor.org']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DBNAME_PRO'),
        'USER': get_secret('DBUSER_PRO'),
        'PASSWORD': get_secret('DBPASSWORD_PRO'),
        'HOST': 'localhost',
        'PORT_PRO': '3306',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# SE DEBE INSTALAR WHITENOISE

STATIC_URL = '/static/'
STATICFILES_URL = '/staticfiles/'
STATICFILES_DIRS = [f'{BASE_DIR}{STATICFILES_URL}', ]
STATIC_ROOT = "/home/fundacio8/fundre/staticfiles"


# LOS MEDIAS DE LA PAGINA

MEDIA_URL = '/media/'
MEDIA_ROOT = "/home/fundacio8/fundre/media"


# ckeditor settings

CKEDITOR_UPLOAD_PATH = 'imagenes/entradas/'
CKEDITOR_IMAGEN_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'


CDKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', ],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-'],
            ['TextColor', 'Format', 'FontSize', 'Link'],
            ['Smiley', 'Image', 'Iframe'],
            ['RemoveFormat', 'Source'],
        ],
        'stylesSet': [
        ],
    }
}

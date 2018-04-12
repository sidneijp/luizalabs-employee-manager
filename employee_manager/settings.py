"""
Django settings for employee_manager project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from decouple import config, Csv
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    'SECRET_KEY', default='wnyyx5y0q)0m(zh221a3r4&&=xlz=xzt$s#_s+6i9k3x)#i1gd'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS', default='localhost, 127.0.0.1', cast=Csv()
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',

    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'employee_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'employee_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

_DB_DEFAULTS = {
    'django.db.backends.sqlite3': {
        'HOST': '',
        'PORT': '',
        'NAME': 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
    },
    'django.db.backends.postgresql': {
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'db.sqlite3',
        'USER': 'postgres',
        'PASSWORD': '',
    },
    'django.db.backends.mysql': {
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'db.sqlite3',
        'USER': 'root',
        'PASSWORD': '',
    },
}

_DB_ENGINE = 'django.db.backends.%s' % config('DB_ENGINE', default='sqlite3')

DATABASES = {
    'default': {
        'ENGINE': _DB_ENGINE,
        'HOST': config('DB_HOST', default=_DB_DEFAULTS[_DB_ENGINE]['HOST']),
        'PORT': config('DB_PORT', default=_DB_DEFAULTS[_DB_ENGINE]['PORT']),
        'NAME': config('DB_NAME', default=_DB_DEFAULTS[_DB_ENGINE]['NAME']),
        'USER': config('DB_USER', default=_DB_DEFAULTS[_DB_ENGINE]['USER']),
        'PASSWORD': config(
            'DB_PASSWORD', default=_DB_DEFAULTS[_DB_ENGINE]['PASSWORD']
        ),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# Django REST Framework settings
# http://www.django-rest-framework.org

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

# Custom settings for DEBUG=True
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += (
        'rest_framework.renderers.BrowsableAPIRenderer',
    )

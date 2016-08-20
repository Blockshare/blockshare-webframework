"""
Django settings for blockshare project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dotenv
import dj_database_url
from two1.wallet import Two1Wallet


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.join(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

TWO1_WALLET_MNEMONIC = os.environ.get("TWO1_WALLET_MNEMONIC")
TWO1_USERNAME = os.environ.get("TWO1_USERNAME")
WALLET = Two1Wallet.import_from_mnemonic(mnemonic=TWO1_WALLET_MNEMONIC)

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')il&@pg6=(^p1%1kr0@0p$3^90i9vlwrukxqth&7z#++kbn2pk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# in settings.py
"""
ALLOWED_HOSTS = [
    'machine-payable.herokuapp.com'
]

DEBUG = os.environ.get("DEBUG", "False").lower() in ['true', '1', 't']
"""

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'blockshare',
    'two1.bitserv.django',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'blockshare.urls'

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

WSGI_APPLICATION = 'blockshare.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC_ROOT = "/blockshare/static"
#STATIC_URL = '/static/'

#STATICFILES_DIRS = ('/root/Business/blockshare/static',)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

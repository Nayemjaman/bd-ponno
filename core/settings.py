"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['bd-ponno.herokuapp.com', '127.0.0.1']

# custom application
CUSTOM_APPS = ['products', 'ponnobot', 'api', ]

PACKAGES = ['rest_framework', 'rest_framework.authtoken', 'corsheaders',
            'django_filters',
            # 'django.contrib.staticfiles', # required for serving swagger ui's css/js files
            # 'drf_yasg',
            ]

# Application definition

INSTALLED_APPS = [
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                 ] + CUSTOM_APPS + PACKAGES

MIDDLEWARE = [
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOW_ALL_ORIGINS = False
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:8000',
# ]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# https://github.com/nesdis/djongo/issues/132
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': str(os.environ.get('DB_NAME')),
        # 'CLIENT': {
        #     'host': 'mongodb+srv://'+str(os.environ.get('DB_USERNAME'))+':'+urllib.parse.quote_plus(str(os.environ.get('DB_PASSWORD'))) +'@cluster0.xcc5n.mongodb.net/test?retryWrites=true&w=majority',
        #     'authMechanism': 'SCRAM-SHA-1'
        # }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',  # todo : remove in production
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

# DATA_UPLOAD_MAX_NUMBER_FIELDS = 50240  # higher than the count of fields

# SSL config
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 518400
# SESSION_COOKIE_SECURE = True
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

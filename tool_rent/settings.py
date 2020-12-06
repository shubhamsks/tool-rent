"""
Django settings for tool_rent project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['TOOL_RENT_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['herokuapp.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    # local
    'tools.apps.ToolsConfig',
    'reviews.apps.ReviewsConfig',
    'users.apps.UsersConfig',

    # Third party
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    'bootstrap_admin',

    # Django
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # for static files
    'storages',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tool_rent.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'tool_rent.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tool_rent',
        'USER': os.environ['TOOL_RENT_DATABASE_USER'],
        'PASSWORD': os.environ['TOOL_RENT_DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
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

# Custom UserModel and AUTH configs

AUTH_USER_MODEL = 'users.User'
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'optional'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'admin@keepborrowuse.com'
# rest_framework token auth configs

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# STATIC FILES ON AWS S3

AWS_ACCESS_KEY_ID = os.environ['TOOL_RENT_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['TOOL_RENT_AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'sk-django-static-s3'

AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_STATICFILES_LOCATION = 'static'
AWS_MEDIAFILES_LOCATION = 'media/'

AWS_S3_HOST = 's3.ap-south-1.amazonaws.com'
AWS_S3_REGION_NAME="ap-south-1"
AWS_QUERYSTRING_AUTH = True
AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = False

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_URL = 'https://{0}/{1}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_STATICFILES_LOCATION)

STATICFILES_STORAGE = 'tool_rent.storage_backends.StaticStorage'

DEFAULT_FILE_STORAGE = 'tool_rent.storage_backends.MediaStorage'


# CORS CONFIGS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://example.com",
    "https://sub.example.com",
    "http://127.0.0.1:9000"
]
# Authentication backends

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

django_heroku.settings(locals())
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


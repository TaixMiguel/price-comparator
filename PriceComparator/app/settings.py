import os
from pathlib import Path

from app.kPriceComparator import Config as ConfigPrice
from app.configApp import ConfigApp

configApp: ConfigApp = ConfigApp()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = configApp.get_value(ConfigPrice.Application.ROOT, ConfigPrice.Application.SECRET_KEY,
                                 'django-insecure-key')
DEBUG = configApp.get_value_boolean(ConfigPrice.Application.ROOT, ConfigPrice.Application.DEBUG_MODE, True)
ALLOWED_HOSTS = configApp.get_value_array(ConfigPrice.Application.ROOT, ConfigPrice.Application.ALLOWED_HOSTS)
CORS_ALLOWED_ORIGINS = configApp.get_value_array(ConfigPrice.Application.ROOT,
                                                 ConfigPrice.Application.CORS_ALLOWED_ORIGINS)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
    'corsheaders',
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

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': configApp.get_value(ConfigPrice.BBDD.ROOT, ConfigPrice.BBDD.ENGINE, 'django.db.backends.sqlite3'),
        'NAME': configApp.get_value(ConfigPrice.BBDD.ROOT, ConfigPrice.BBDD.NAME, f'{BASE_DIR}/config/db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'es-es'
TIME_ZONE = os.environ.get('TZ', 'UTC')
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

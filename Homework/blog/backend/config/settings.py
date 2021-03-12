import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# DEBUG = os.getenv("DJANGO_DEBUG", default=False)

# ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", default="*,").split(',')

SECRET_KEY = 'awdwnrrm*b9*5649xgva6=*amzb&7(7w7!cam^^d^=n-j780bh'

DEBUG = 'True'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.postgresql",
        # "NAME": os.getenv("DB_NAME", default="postgres"),
        # "USER": os.getenv("DB_USER", default="postgres"),
        # "PASSWORD": os.getenv("DB_PASSWORD", default="postgregs"),
        # "HOST": os.getenv("DB_HOST", default="postgres"),
        # "PORT": os.getenv("DB_PORT", default="postgres"),
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'skill_up',
        "USER": 'super_user',
        "PASSWORD": '1',
        "HOST": '127.0.0.1',
        "PORT": '5432',
    }
}

# Password validation

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

# Media

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
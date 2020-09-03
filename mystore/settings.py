import os
# message import
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+*5oo56c#!tvvg@0ssxrhj223tz@53taocrhww6^od%m&_2t0j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop.apps.ShopConfig',  # shop app
    'cart.apps.CartConfig',  # cart app
    'orders.apps.OrdersConfig',  # orders app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # makes current session available in the request object.
    # You can access the current session using request.session, it acts like a Python
    # dictionary to store and retrieve session data.
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mystore.urls'

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

                'cart.context_processors.cart',  # cart context_processors
            ],
        },
    },
]

WSGI_APPLICATION = 'mystore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# location of 'static' in mystore folder
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "mystore/static"),
]

# creates 'static' folder in the root dir (OnlineStore) after running collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# LOGIN_REDIRECT_URL = 'post_list'

# LOGOUT_REDIRECT_URL = '/login/'

# LOGIN_URL = '/login/'

# media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # creates a 'media' folder in the root dir (Housing) directory

# cart session key
CART_SESSION_ID = 'cart'

# messages
MESSAGE_TAGS = {
    messages.ERROR: 'alert-danger',  # value is equal to the bootstrap class of 'alert-danger'
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


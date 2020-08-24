"""
Django settings for python_sitesi project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y5s(@x(xo@hi#s#7pg638s48!2k%^^s*nqx225p%0$!s+fxlcn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.pythonakademi.com']
#ALLOWED_HOSTS = []
INTERNAL_IPS = [
	'127.0.0.1',
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
	'django.contrib.sites',
	'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.admindocs',
	'django.contrib.flatpages',
	'django.contrib.humanize',
	'django.contrib.redirects',
	#my apps
	'hakkimizda',
	'ingilizce',
	'tur',
	'denemeler',
	'core',
	#3.parti uygulamalar
	'crispy_forms',
	'ckeditor',
	'captcha',
	#'debug_toolbar',
]

SITE_ID = 1

MIDDLEWARE = [
	#'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
	
]

ROOT_URLCONF = 'python_sitesi.urls'

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

WSGI_APPLICATION = 'python_sitesi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

CRISPY_TEMPLATE_PACK = "bootstrap3"
CKEDITOR_jQUERY_URL = os.path.join(STATIC_URL, "js/jquery.min.js")

CKEDITOR_CONFIGS = {
	'default': {
		'toolbar': 'full',
		'width':'100%',
		'extraPlugins': '.'.join(
		[ 
			'codesnippet',
		]),
		'codeSnippet_languages': {
			'python': 'Python',
			'bash': "Bash",
			'html': "HTML",
		},
	},
}

RECAPTCHA_PUBLIC_KEY = '6Lf64pUUAAAAAIDe__tdy73eA2-2K3sYfakuCqQw'
RECAPTCHA_PRIVATE_KEY = '6Lf64pUUAAAAAAz4zzOsS2WI5CGsQkYLW35M2xXI'
NOCAPTCHA= True



LANGUAGES = [
('tr', 'Turkish'),
('en', 'English'),
]

#SESSION_COOKIE_AGE = 3



from .lokal import *
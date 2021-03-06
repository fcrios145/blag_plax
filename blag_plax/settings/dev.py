"""
Django settings for template project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o0s-w4c3ud4b9%gz4@4z6878x#8xznh0c7kv-+g#@a-_81__e1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # aplicaciones que creamos nosotros, las tenemos que agregar en esta parte
    'blog',
    'pipeline',
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

ROOT_URLCONF = 'blag_plax.urls'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blag_plax',
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

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

WSGI_APPLICATION = 'blag_plax.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/webapps/blag_plax/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_UGLIFYJS_BINARY = '/usr/bin/uglifyjs'

# CSS Files.
PIPELINE_CSS = {
    # Project libraries.
    'libraries': {
        'source_filenames': (
            'main/reset.css',
            'main/main.css',
        ),
        'output_filename': 'css/libs.min.css',
    },
    'bootstrap': {
        'source_filenames': (
            'bower_components/normalize-css/normalize.css',
            'bower_components/bootstrap/dist/css/bootstrap.css',
            'main/bmain.css',
        ),
        'output_filename': 'css/bootstrap.min.css',
    },
    'foundation': {
        'source_filenames': (
            'bower_components/normalize-css/normalize.css',
            'main/app.sass',
        ),
        'output_filename': 'css/foundation.min.css',
    }
}

# JavaScript files.
PIPELINE_JS = {
    # Project JavaScript libraries.
    'libraries': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.js',
            'bower_components/underscore/underscore.js',
            'bower_components/modernizr/modernizr.js',
            'bower_components/bootstrap/dist/js/bootstrap.js',
        ),
        # Compress all passed files into `js/libs.min.js`.
        'output_filename': 'js/libs.min.js',
    }
    # ...
}

PIPELINE_COMPILERS = (
    # 'pipeline.compilers.coffee.CoffeeScriptCompiler',
    'pipeline.compilers.sass.SASSCompiler',
    # 'pipeline.compilers.stylus.StylusCompiler',
)
# PIPELINE_COFFEE_SCRIPT_BINARY = '/usr/bin/coffee'
PIPELINE_SASS_BINARY = '/usr/local/rvm/gems/ruby-2.2.1/bin/sass'
# PIPELINE_STYLUS_BINARY = '/usr/bin/stylus'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from configurations import Configuration, values
import dj_database_url
from django.conf.global_settings import DATABASES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

project = 'nellyshulman'


class Base(Configuration):
    SECRET_KEY = os.environ['SECRET_KEY']
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
        'raven.contrib.django.raven_compat',
        'debug_toolbar',
        'easy_thumbnails',
        'storages',
        'main',
        'blog',
    ]

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',

    )

    ROOT_URLCONF = 'nellyshulman.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    WSGI_APPLICATION = 'nellyshulman.wsgi.application'
    RAVEN_CONFIG = {
        'dsn': os.getenv('SENTRY_DSN'),

    }
    ATOMIC_REQUESTS = values.BooleanValue(True)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',

    ]
    THUMBNAIL_ALIASES = {
        '': {
            'avatar': {'size': (50, 50), 'crop': True},
            'picture': {'size': (800, 500), 'crop': True},
            'large': {'size': (800, 600), 'crop': True},
        },
    }


class Development(Base):
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nelly',
        'USER': 'postgres',
        }
    }
    DEBUG = values.BooleanValue(True)

    STATIC_ROOT = os.path.join(BASE_DIR, 'nellyshulman/static')
    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'nellyshulman/media')
    MEDIA_URL = '/media/'


class Production(Base):
    THUMBNAIL_DEFAULT_STORAGE = '%s.s3.Media' % project
    DEBUG = values.BooleanValue(False)
    ALLOWED_HOSTS = ['*']

    DATABASES['default'] = dj_database_url.config(conn_max_age=600)

    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_AUTO_CREATE_BUCKET = values.BooleanValue(True)
    AWS_QUERYSTRING_AUTH = False

    COMPRESS_STORAGE = '%s.s3.Static' % project

    DEFAULT_FILE_STORAGE = '%s.s3.Media' % project
    STATICFILES_STORAGE = '%s.s3.CachedS3BotoStorage' % project
    MEDIA_S3 = 'media'
    STATIC_S3 = 'static'
    MEDIA_ROOT = '/%s/' % MEDIA_S3
    STATIC_ROOT = '/%s/' % STATIC_S3
    MEDIA_URL = 'https://%s.s3.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME, MEDIA_S3)
    STATIC_URL = "https://%s.s3.amazonaws.com/%s/" % (AWS_STORAGE_BUCKET_NAME, STATIC_S3)
    COMPRESS_URL = STATIC_URL

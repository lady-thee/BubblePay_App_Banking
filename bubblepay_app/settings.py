

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mqp21l#%12a3uz^ea$sm-c&zq2z=hhkql&4c7fc9rj9n60zh2q'

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

    'home_app.apps.HomeAppConfig',
    'customers_app.apps.CustomersAppConfig',
    'dashboard.apps.DashboardConfig',
    'transactions.apps.TransactionsConfig',

    'compressor',
    'phonenumber_field',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware', 
    'htmlmin.middleware.HtmlMinifyMiddleware', 
    'htmlmin.middleware.MarkRequestMiddleware', 

    #DataFlair #Caching Middleware

    'django.middleware.cache.UpdateCacheMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.cache.FetchFromCacheMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bubblepay_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates/'],
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



# CACHE MEMCACHED

CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'LOCATION': ['unix:/tmp/memcached.sock','127.0.0.1:11211'],
    # }
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

WSGI_APPLICATION = 'bubblepay_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bubblepay_db',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PASSWORD': '2030',
        'PORT': '5432'
    }
}
# AUTH USER MODEL 
AUTH_USER_MODEL = 'customers_app.Users'

LOGIN_REDIRECT_URL = "login"
LOGOUT_REDIRECT_URL = "login"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# EMAIL MESSAGE SETTINGS

EMAIL_ACTIVE_FIELD = 'is_email_verified'
EMAIL_HOST = 'smtp.gmail.com'  #email of python email handler
EMAIL_HOST_USER = 'webservices135@gmail.com' #your email. It will be a default email if a sender is not specified
EMAIL_HOST_PASSWORD = 'qjeiflcrlrpladxk'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static/'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')



# MEDIA FILES(User's photo), Media Roots

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') 


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    
    'compressor.finders.CompressorFinder',
)

# COMPRESS MIDDLEWARE AND HTMLMINIFY
COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

# COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', default=True)
# COMPRESS_CSS_HASHING_METHOD = 'content'
# COMPRESS_OFFLINE = True
# COMPRESS_OFFLINE_MANIFEST = 'compressor_manifest.json'
# COMPRESS_PARSER = 'compressor.parser.HtmlParser'
# COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
COMPRESS_FILTERS = {
    'css':[
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter',
    ],
    'js':[
        'compressor.filters.jsmin.JSMinFilter',
    ]
}
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = True


# whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
Django settings for qp project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import django_heroku
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2bzp&z&ou_i-dw^b-wy6cv+m##8!6rdcll9+%p0b-ar1gc^f+9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['qpworld.herokuapp.com/','127.0.0.1','questionpaper.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # own apps
    'question_papers.apps.QuestionPapersConfig',
    'profiles.apps.ProfilesConfig',
    'users.apps.UsersConfig',
    'contacts.apps.ContactsConfig',
    'provides.apps.ProvidesConfig',
    'provides_controller.apps.ProvidesControllerConfig',

    # Thirdparty apps
    'cloudinary_storage',
    'cloudinary',

]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET')
}
 

MIDDLEWARE = [
    # SecurityMiddleware must be listed before other middleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

ROOT_URLCONF = 'qp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'qp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'qp',
        'USER': 'postgres',
        'PASSWORD': 'vigneshnu77',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)



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

#Email Configarations
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = '/media/'  # or any prefix you choose
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# MEDIA_URL = '/media/'
# MEDIA_ROOT =os.path.join(BASE_DIR,'media')

django_heroku.settings(locals())







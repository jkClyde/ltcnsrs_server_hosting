"""
Django settings for LTCNSRS project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
# import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2$51go25%0zvue#0gvz0*p!i%#++af)xm%e33-nlfpnp^!^q1-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.137.1', '192.168.100.114']
ALLOWED_HOSTS = ['ltcnsrs.onrender.com', 'http://localhost:5173', 'ltcnsrs-server.onrender.com', 'ltcnsrs.netlify.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #My Apps
    # 'app_calendar.apps.AppCalendarConfig',
    'rest_framework',
    'corsheaders',
    'app_form',
    'rest_framework_simplejwt',
    'djoser',
    'app_accounts.apps.AppAccountsConfig',
    'app_calendar.apps.AppCalendarConfig',
    'app_audit.apps.AppAuditConfig',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),  # Set the lifespan to 1 hour
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #MY MIDDLEWARE
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'LTCNSRS.urls'

CSRF_COOKIE_SECURE = True

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

WSGI_APPLICATION = 'LTCNSRS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'db_ltcnsrs',
    #     'USER': 'postgres_user',
    #     'PASSWORD': 'iAFqCiK1KrLZtHTmgYb0pjWq6502ohtm',
    #     'HOST': 'dpg-cmr2ebq1hbls73fmqnlg-a.singapore-postgres.render.com',
    #     'PORT': '5432',
    # }

     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_ltcnsrs',
        'USER': 'postgres',
        'PASSWORD': 'clyderz1232123',
        'HOST': 'db-ltcnsrs.c5i0qqgoq3sa.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
     }
}




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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Add your frontend URL here
    "https://ltcnsrs-server.onrender.com",
    "https://ltcnsrs.onrender.com",
    "https://ltcnsrs.netlify.app",
    'http://db-ltcnsrs.c5i0qqgoq3sa.us-east-2.rds.amazonaws.com',
    'https://db-ltcnsrs.c5i0qqgoq3sa.us-east-2.rds.amazonaws.com',
]



#EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'lt.cnsrs@gmail.com'
EMAIL_HOST_PASSWORD = 'sfqk qtci ekly pybx'
EMAIL_USE_TLS = True

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': False,  # Disable email confirmation on user creation
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/users/activation/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,  # Disable email activation
    'SERIALIZERS': {
        'user_create': 'app_accounts.serializers.UserCreateSerializer',
        'user': 'app_accounts.serializers.UserCreateSerializer',
        'current_user': 'app_accounts.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}


AUTHENTICATION_BACKENDS = [
    'app_accounts.CustomBackend.CustomBackend',  # Replace 'path.to' with the actual import path to your CustomBackend class
    # Other authentication backends (if any)
]


AUTH_USER_MODEL = 'app_accounts.UserAccount'

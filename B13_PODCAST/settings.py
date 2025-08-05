import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-django-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # Third-party
    'allauth',
    'allauth.account',
    'storages',
    
    # Local apps
    'users',
    'podcasts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'B13_PODCAST.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'B13_PODCAST.wsgi.application'

# Supabase Config
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://raoqkgrtyyowjvkynglo.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJhb3FrZ3J0eXlvd2p2a3luZ2xvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQ0MjE0MzAsImV4cCI6MjA2OTk5NzQzMH0.uvHc0RD21c1kl0v1LmM2CDeALvAZaoLD61KK7Ha6hUo")
PROJECT_ID = os.environ.get("PROJECT_ID", "raoqkgrtyyowjvkynglo")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "your-db-password")
SERVICE_ROLE_KEY = os.environ.get("SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJhb3FrZ3J0eXlvd2p2a3luZ2xvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NDQyMTQzMCwiZXhwIjoyMDY5OTk3NDMwfQ.o31es3lHALL-bHZAqbgClQh_uKWuYLEeov1sFIvPmMo")

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': DB_PASSWORD,
        'HOST': f'{PROJECT_ID}.supabase.co',
        'PORT': '5432',
    }
}

# Storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = SUPABASE_KEY
AWS_SECRET_ACCESS_KEY = SERVICE_ROLE_KEY
AWS_STORAGE_BUCKET_NAME = 'b13-podcast'
AWS_S3_ENDPOINT_URL = f'https://{PROJECT_ID}.supabase.co/storage/v1'
AWS_S3_CUSTOM_DOMAIN = f'{PROJECT_ID}.supabase.co/storage/v1/object'
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False

# Authentication
AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files (uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
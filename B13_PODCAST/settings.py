import os

# Supabase Config
SUPABASE_URL = os.environ.get("https://raoqkgrtyyowjvkynglo.supabase.co")
SUPABASE_KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJhb3FrZ3J0eXlvd2p2a3luZ2xvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQ0MjE0MzAsImV4cCI6MjA2OTk5NzQzMH0.uvHc0RD21c1kl0v1LmM2CDeALvAZaoLD61KK7Ha6hUo")
PROJECT_ID = os.environ.get("raoqkgrtyyowjvkynglo")

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': f'db.{PROJECT_ID}.supabase.co',
        'PORT': '5432',
    }
}

# Storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = SUPABASE_KEY
AWS_SECRET_ACCESS_KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJhb3FrZ3J0eXlvd2p2a3luZ2xvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NDQyMTQzMCwiZXhwIjoyMDY5OTk3NDMwfQ.o31es3lHALL-bHZAqbgClQh_uKWuYLEeov1sFIvPmMo")
AWS_STORAGE_BUCKET_NAME = 'b13-podcast'
AWS_S3_ENDPOINT_URL = f'https://raoqkgrtyyowjvkynglo.storage.supabase.co/storage/v1/s3/'

AUTH_USER_MODEL = 'users.CustomUser'
INSTALLED_APPS = [
    # ...
    'allauth',
    'allauth.account',
    'users',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = 'home'
ACCOUNT_EMAIL_REQUIRED = True
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['itter.pythonanywhere.com', 'aws-0-us-east-1.pooler.supabase.com', 'codecooker1.github.io']

CORS_ALLOWED_ORIGINS = ["https://codecooker1.github.io"]  # We add your frontend URL here.
CORS_ORIGIN_WHITELIST = ['https://codecooker1.github.io',]
CSRF_TRUSTED_ORIGINS = ["https://codecooker1.github.io"]  # We add your frontend URL here.
SESSION_COOKIE_DOMAIN="codecooker1.github.io"
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = 'None'

MIDDLEWARE = [
    'itter_backend.middleware.CookiePartitioningMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_PARTITIONED = True
CORS_ALLOWS_CREDENTIALS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
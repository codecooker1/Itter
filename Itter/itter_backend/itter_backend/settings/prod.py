from .base import *

DEBUG = False

ALLOWED_HOSTS = ['itter.pythonanywhere.com', 'aws-0-us-east-1.pooler.supabase.com', 'codecooker1.github.io']

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
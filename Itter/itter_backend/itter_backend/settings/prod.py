from .base import *

DEBUG = False

ALLOWED_HOSTS = ['itter.pythonanywhere.com', 'aws-0-us-east-1.pooler.supabase.com', 'codecooker1.github.io']

CORS_ALLOWED_ORIGINS = ["https://codecooker1.github.io", "https://itter.pythonanywhere.com"]  # We add your frontend URL here.
CSRF_TRUSTED_ORIGINS = ["https://codecooker1.github.io", "https://itter.pythonanywhere.com"]  # We add your frontend URL here.
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True
CORS_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_PARTITIONED = True
CORS_ALLOWS_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
"accept",
"accept-encoding",
"authorization",
"content-type",
"dnt",
"origin",
"user-agent",
"x-csrftoken",
"x-requested-with",
"sessionid",
"set-cookie",
] 

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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

# Use pythonanywhere's database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': f'{env["DB_NAME_PROD"]}',
        'USER': f'{env["DB_USER_PROD"]}',
        'PASSWORD': f'{env["DB_PASS_PROD"]}',
        'HOST': f'{env["DB_HOST_PROD"]}',
    }
}
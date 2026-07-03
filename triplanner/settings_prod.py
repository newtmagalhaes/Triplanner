from os import environ, getenv

from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ['SECRET_KEY']
SECRET_KEY_FALLBACKS = getenv("OLD_SECRET_KEY", '').split()

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_NAME = 'triplanner.session.prod'
CSRF_COOKIE_NAME = 'triplanner.csrf.prod'
CSRF_COOKIE_SECURE = True
URLIZE_ASSUME_HTTPS = True
USE_X_FORWARDED_HOST = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split()

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

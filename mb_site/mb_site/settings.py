import os
import importlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Defaults that can be overridden from `config` package or env
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-dev-secret-key')
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mb_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'board' / 'templates'],
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

WSGI_APPLICATION = 'mb_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'board' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Load optional config from `config` package (e.g. config.default)
# Set `APP_CONFIG_MODULE` env var to choose a module path (default: 'config.default')
APP_CONFIG_MODULE = os.environ.get('APP_CONFIG_MODULE', 'config.default')
try:
    cfg = importlib.import_module(APP_CONFIG_MODULE)
except Exception:
    cfg = None

if cfg:
    SECRET_KEY = getattr(cfg, 'SECRET_KEY', SECRET_KEY)
    DEBUG = getattr(cfg, 'DEBUG', DEBUG)
    # Map a simple SQLAlchemy-style sqlite URI if provided in the config
    dburi = getattr(cfg, 'SQLALCHEMY_DATABASE_URI', None)
    if dburi and isinstance(dburi, str) and dburi.startswith('sqlite:///'):
        # strip prefix and use that path as sqlite DB
        db_path = dburi.replace('sqlite:///', '')
        DATABASES['default']['NAME'] = Path(db_path)

# Auth redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'posts'
LOGOUT_REDIRECT_URL = 'home'

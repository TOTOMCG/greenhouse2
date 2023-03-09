from pathlib import Path, os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "DJANGO-SECRET-DEDKOV-POMIDORY-TREUGOLNY-PASSWORD-KEY-#$%^)$()-g^2612-mn$772-g2g312"
DEBUG = True

ALLOWED_HOSTS = ['10.10.10.55', '127.0.0.1']

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "main",
    "utility",
    "django_celery_beat"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "greenhouse.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'templates')
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_URL = "static/"

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# MEDIA_URL = '/media/'

WSGI_APPLICATION = "greenhouse.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "ru"
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = "Europe/Moscow"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BROKER_URL = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'
accept_content = ['application/json']
result_serializer = 'json'
task_serializer = 'json'
timezone = "Europe/Moscow"

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "++++++++++++++++++++++++++++++++++++++++++++++++++"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_zarinpal",
]

SITE_ID = 1

# django_zarinpal settings
ZARINPAL_SIMULATION = True
ZARINPAL_CALLBACK_URL = "localhos:8000/callback"

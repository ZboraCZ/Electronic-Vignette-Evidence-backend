# -*- coding: utf-8 -*-
"""
Django settings for eve project.

Generated by "django-admin startproject" using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import sys
from pathlib import Path

from eve.utils import config_from_envvar, getenv_bool, getenv_list

if not config_from_envvar("EVE_CONFIG"):
    print("Missing 'EVE_CONFIG' envvar")
    sys.exit(1)

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = getenv_bool("DEBUG")


ALLOWED_HOSTS = getenv_list("ALLOWED_HOSTS")

# CORS cofiguration
CORS_ALLOWED_ORIGINS = getenv_list("CORS_ALLOWED_ORIGINS")
CORS_ALLOW_ALL_ORIGINS = getenv_bool("CORS_ALLOW_ALL_ORIGINS")

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
    "eve.vignettes",
    "eve.users",
    "corsheaders",
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "eve.urls"


WSGI_APPLICATION = "eve.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": int(os.getenv("DB_PORT")),
    }
}


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
}


TIME_ZONE = "UTC"


USE_TZ = True

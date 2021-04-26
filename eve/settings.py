# -*- coding: utf-8 -*-

import os

from pathlib import Path

from eve.utils import config_from_envvar, getenv_bool, getenv_list

if not config_from_envvar("EVE_CONFIG"):
    print("Missing 'EVE_CONFIG' envvar. Using production settings.")
    DEBUG = False
else:
    DEBUG = getenv_bool("DEBUG")


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")


ALLOWED_HOSTS = getenv_list("ALLOWED_HOSTS")


CORS_ALLOW_ALL_ORIGINS = getenv_bool("CORS_ALLOW_ALL_ORIGINS")


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
    "eve.vignettes",
    "eve.users",
    "eve.roles",
    "eve.statistics",
    "eve.authentication",
    "corsheaders",
    "rest_framework.authtoken"
]

AUTH_USER_MODEL = "users.Users"

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
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ]
}


TEMPLATES_DIR = os.path.join(BASE_DIR, "eve", "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
    }
]


TIME_ZONE = "UTC"


USE_TZ = True

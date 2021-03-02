# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv


def config_from_envvar(env_var):
    path = os.getenv(env_var, "")
    if os.path.exists(path) and os.path.isfile(path):
        load_dotenv(path)
        return True

    return False


def getenv_bool(env_var, default=None):
    if var := os.getenv(env_var):
        return var in ("True", "true")

    return default


def getenv_list(env_var, default=None, delimiter=" "):
    if var := os.getenv(env_var):
        return var.split(delimiter)

    return default

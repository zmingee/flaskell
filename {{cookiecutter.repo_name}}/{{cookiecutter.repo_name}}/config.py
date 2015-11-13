# -*- coding: utf-8 -*-
"""
    {{cookiecutter.repo_name}} default and base Flask configurations
"""

# pylint: disable=too-few-public-methods

import os

from .utils import make_dir, INSTANCE_FOLDER_PATH


class BaseConfig(object):
    """
    Base Configuration for Flask. Applies to all applications using
    :class:`{{cookiecutter.repo_name}}.helpers.configure_app()`
    """

    PROJECT = "{{cookiecutter.repo_name}}"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    ADMINS = ['{{cookiecutter.email}}']

    SECRET_KEY = 'secret key'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    make_dir(LOG_FOLDER)


class DefaultConfig(BaseConfig):
    """
    Configuration object from :class:`{{cookiecutter.repo_name}}.config.BaseConfig` for
    production Flask apps. Applies to all applications using
    :method:`{{cookiecutter.repo_name}}.helpers.configure_app()`
    """

    DEBUG = False


class TestConfig(BaseConfig):
    """
    Configuration object from :class:`{{cookiecutter.repo_name}}.config.BaseConfig`
    Configuration for Flask. Applies to all applications using
    :method:`{{cookiecutter.repo_name}}.helpers.configure_app()`
    """

    TESTING = True
    WTF_CSRF_ENABLED = False

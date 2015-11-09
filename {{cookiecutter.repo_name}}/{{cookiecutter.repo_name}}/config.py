"""
    {{cookiecutter.repo_name}} default and base Flask configurations
"""


# -*- coding: utf-8 -*-
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

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
    make_dir(UPLOAD_FOLDER)


class DefaultConfig(BaseConfig):
    """
    Configuration object from :class:`{{cookiecutter.repo_name}}.config.BaseConfig` for
    production Flask apps. Applies to all applications using
    :method:`{{cookiecutter.repo_name}}.helpers.configure_app()`
    """

    DEBUG = False

    # Flask-Sqlalchemy
    #SQLALCHEMY_ECHO = True
    # SQLITE for prototyping.
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH + '/db.sqlite'
    # MYSQL for production.
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60


class TestConfig(BaseConfig):
    """
    Configuration object from :class:`{{cookiecutter.repo_name}}.config.BaseConfig`
    Configuration for Flask. Applies to all applications using
    :method:`{{cookiecutter.repo_name}}.helpers.configure_app()`
    """

    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

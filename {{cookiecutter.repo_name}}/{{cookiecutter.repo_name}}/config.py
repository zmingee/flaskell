"""
{{cookiecutter.repo_name|capitalize}} default and base Flask configurations
"""

# pylint: disable=too-few-public-methods

import os

from .utils import make_dir


class BaseConfig(object):
    """
    Base Configuration for Flask. Applies to all applications using
    :class:`{{cookiecutter.repo_name}}.factory.configure_app()`
    """

    PROJECT = "{{cookiecutter.repo_name}}"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    ADMINS = ['{{cookiecutter.email}}']

    INSTANCE_FOLDER_PATH = os.path.join('/etc', '{{cookiecutter.repo_name}}')
    make_dir(INSTANCE_FOLDER_PATH)
    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    make_dir(LOG_FOLDER)

    DEBUG = False
    TESTING = False


class DefaultConfig(BaseConfig):
    """
    Configuration object from :class:`{{cookiecutter.repo_name}}.config.BaseConfig` for
    production Flask apps. Applies to all applications using
    :method:`{{cookiecutter.repo_name}}.factory.configure_app()`
    """

    LOGLEVEL = 'DEBUG'

    SECRET_KEY = 'SUPERSECRET'


class ProductionConfig(BaseConfig):
    """
    Configuration object from :class:`{{cookiecutter.repo_name}}.config.BaseConfig` for
    production Flask apps. Applies to all applications using
    :method:`{{cookiecutter.repo_name}}.factory.configure_app()`
    """

    LOGLEVEL = 'INFO'

    SECRET_KEY = 'VERYSUPERSECRET'


class TestConfig(BaseConfig):
    """
    Configuration object from :class:`{{cookiecutter.repo_name}}.config.BaseConfig`
    Configuration for Flask. Applies to all applications using
    :method:`{{cookiecutter.repo_name}}.factory.configure_app()`
    """

    DEBUG = True
    TESTING = True

# -*- coding: utf-8 -*-
"""
    {{cookiecutter.repo_name}} factory module for generating objects and apps
"""

from flask import Flask
#from celery import Celery

from .helpers import (configure_app, configure_blueprints, configure_extensions, configure_logging)
from .utils import INSTANCE_FOLDER_PATH

# TODO: Integrate Celery into app for jobs

def create_app(repo_name, package_path, settings_override=None):
    """
    Returns a :class:`Flask` application instance configured with common
    functionality for the Compute

    :param str repo_name: Name to assign to :class:`flask.Flask`
    :param str package_path: Path of package to pass to
                             :class:`{{cookiecutter.repo_name}}.helpers.configure_blueprints` so
                             blueprints can be auto-registered
    :param dict settings_override: A dictionary of settings to override

    :return: Flask app
    :rtype: :class:`flask.Flask`
    """


    app = Flask(repo_name, instance_path=INSTANCE_FOLDER_PATH,
                instance_relative_config=True)

    configure_app(app, settings_override)

    configure_logging(app)

    app.logger.debug('Built and configured app: `%s`', app.name)

    app.logger.debug('Configuring extensions for `%s`', app.name)
    configure_extensions(app)

    app.logger.debug('Configuring blueprints for `%s`', app.name)
    configure_blueprints(app, repo_name, package_path)

    return app

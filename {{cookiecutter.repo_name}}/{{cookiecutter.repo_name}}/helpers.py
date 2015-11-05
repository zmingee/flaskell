# -*- coding: utf-8 -*-
"""
    {{cookiecutter.repo_name}} helpers module with various modularized methods for
    configuring Flask apps using :method:`{{cookiecutter.repo_name}}.factory.create_app()`
"""

import os
import pkgutil
import importlib

from flask import Blueprint

from .config import DefaultConfig
from .extensions import (JSONRPC)


def configure_app(app, settings_override=None):
    """
    Configure Flask application container in the following order:
        - :class:`{{cookiecutter.repo_name}}.config.DefaultConfig` (which inherits from
        :class:`{{cookiecutter.repo_name}}.config.BaseConfig`
        - production.cfg
        - ``config`` param

    :param app: Flask app object to configure
    :type app: :class:`flask.Flask`
    :param dict settings_override: a dictionary of settings to override

    :return: Does not return
    """

    app.config.from_object(DefaultConfig)

    app.config.from_pyfile('production.cfg', silent=True)

    if settings_override:
        app.config.from_object(settings_override)


def configure_blueprints(app, repo_name, package_path):
    """
    Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: Flask app object to configure
    :type app: :class:`flask.Flask`
    :param str repo_name: Name to assign to :class:`flask.Flask`
    :param str package_path: Path of package to pass to so
                             blueprints can be auto-registered

    :return: List of blueprints found and registered
    :rtype: list
    """

    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        module = importlib.import_module('%s.%s' % (repo_name, name))
        for item in dir(module):
            item = getattr(module, item)
            if isinstance(item, Blueprint):
                app.logger.debug('Registering blueprint `%s` for app `%s`', item.name, app.name)
                app.register_blueprint(item)
            rv.append(item)
    return rv


def configure_extensions(app):
    """
    Configure extensions for passed Flask app

    :param app: Flask app object to configure
    :type app: :class:`flask.Flask`
    :return: Does not return
    """

    # TODO: Change explicitly defined extensions to something similar to configure_blueprints

    app.logger.debug('Configuring app `%s` for Flask-JSONRPC', app.name)
    JSONRPC.init_app(app)


def configure_logging(app):
    """
    Configures logging methods for Flask app

    :param app: Flask app object to configure
    :type app: :class:`flask.Flask`

    :return: Does not return
    """

    if app.debug or app.testing:
        return

    import logging
    import logging.handlers

    app.logger.setLevel(logging.DEBUG)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = logging.handlers.RotatingFileHandler(info_log,
                                                             maxBytes=100000,
                                                             backupCount=10)
    info_file_handler.setLevel("DEBUG")
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s: %(levelname)-8s: %(pathname)s:%(funcName)s:%(lineno)d :: %(message)s'))
    app.logger.addHandler(info_file_handler)

    from logging import getLogger
    loggers = [getLogger('werkzeug')]
    for logger in loggers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(info_file_handler)

    # Testing
    #app.logger.info("testing info.")
    #app.logger.warn("testing warn.")
    #app.logger.error("testing error.")

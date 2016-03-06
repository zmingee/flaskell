"""
{{cookiecutter.repo_name|capitalize}} factory module for generating objects and apps
"""

import os
import pkgutil
import importlib
import logging
import logging.handlers

from cloghandler import ConcurrentRotatingFileHandler
from flask import Flask, Blueprint

from .config import DefaultConfig
from .extensions iport JSONRPC

LOGGER = logging.getLogger(__name__)


def create_app(package_name, package_path, settings_override=None):
    """
    Returns a fully configured :class:`Flask` application instance

    :param str package_name: Name to assign to :class:`flask.Flask`
    :param str package_path: Path of package to pass to
        :class:`{{cookiecutter.repo_name}}.helpers.configure_blueprints` so
        blueprints can be auto-registered
    :param dict settings_override: A dictionary of settings to override
    :return: Flask app
    :rtype: :class:`flask.Flask`
    """


    app = Flask(
        package_name,
        instance_path=DefaultConfig.INSTANCE_FOLDER_PATH,
        instance_relative_config=True
    )

    configure_app(app, settings_override)
    configure_logging(app)
    LOGGER.info('Built and configured app:`%s`', app.name)
    configure_extensions(app)
    LOGGER.info('Configured extensions for app:`%s`', app.name)
    configure_blueprints(app, package_name, package_path)
    LOGGER.info('Configured blueprints for app:`%s`', app.name)

    return app


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
                LOGGER.debug('Registering blueprint:`%s` for app:`%s`', item.name, app.name)
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

    LOGGER.info('Configuring app:`%s` for Flask-JSONRPC', app.name)
    JSONRPC.init_app(app)


def configure_logging(app):
    """
    Configures logging methods for Flask app

    :param app: Flask app object to configure
    :type app: :class:`flask.Flask`
    :return: Does not return
    """

    module_loggers = [
        app.logger,
        logging.getLogger('werkzeug'),
        logging.getLogger('{{cookiecutter.repo_name}}'),
    ]

    formatter = '%(asctime)s: %(levelname)-8s: %(module)s:%(funcName)s:%(lineno)d :: %(message)s'

    log_file = os.path.join(app.config['LOG_FOLDER'], 'app.log')
    file_handler = logging.handlers.ConcurrentRotatingFileHandler(
        log_file,
        maxBytes=100000,
        backupCount=10
    )
    file_handler.setLevel('DEBUG')
    file_handler.setFormatter(logging.Formatter(formatter))

    console_handler = logging.StreamHandler()
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(logging.Formatter(formatter))

    for module_logger in module_loggers:
        module_logger.setLevel(logging.DEBUG)
        module_logger.addHandler(file_handler)
        if not app.config['TESTING']:
            module_logger.addHandler(console_handler)

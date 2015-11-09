#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os

from flask import Flask

from .config import DefaultConfig
from .extensions import jsonrpc
from .api import api
from .utils import INSTANCE_FOLDER_PATH


DEFAULT_BLUEPRINTS = (
    api,
)

def create_app(config=None, app_name=None, blueprints=None):
    """Flask app factory."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)
    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app, blueprints)

    return app

def configure_app(app, config=None):
    """Different ways of configurations."""

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    # http://flask.pocoo.org/docs/cofnfig/#instance-folders
    app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)

    # Use instance folder instead of env variables to make deployment easier.
    #app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)

def configure_extensions(app):

def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)



def configure_logging(app):
    """Configure file logging."""

    # if app.debug or app.testing:
    #     # Skip debug and test mode. Just check standard output.
    #     return

    import logging

    app.logger.setLevel("INFO")

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')

    info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel("INFO")
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )



    app.logger.addHandler(info_file_handler)
    # Testing
    #app.logger.info("testing info.")
    #app.logger.warn("testing warn.")
    #app.logger.error("testing error.")
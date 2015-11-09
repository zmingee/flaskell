# -*- coding: utf-8 -*-
"""
    {{cookiecutter.repo_name}}.api
    ################

    API sub-app package implemented via JSON-RPC
"""

from functools import wraps

from flask import jsonify

from .. import factory
from ..core import ComputeError, ComputeFormError
from ..utils import JSONEncoder
from ..extensions import JSONRPC


def create_app(settings_override=None):
    """ Uses app factory to generate Flask app for blueprints in sub-app

    :param dict settings_override: Dictionary of settings to override

    :return: Flask sub-app for JSON-RPC API
    :rtype: :class:`flask.Flask`
    """

    app = factory.create_app(__name__, __path__, settings_override)


    # TODO: Investigate json_encoder change, verify it's needed, and document

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    # TODO: Investigate custom error handlers, verify it's needed, and document

    # Register custom error handlers
    app.logger.debug('Registering error handlers for %s' % app.name)
    app.errorhandler(ComputeError)(on_api_error)
    app.errorhandler(ComputeFormError)(on_api_form_error)
    app.errorhandler(404)(on_404)

    return app


def route(*args, **kwargs):
    """ Wrapper decorator for ``@jsonrpc.method`` so we can chain multiple
    decorators together

    :param args: args to pass to decorator(s)
    :param kwargs: kwargs to pass to decorator(s)

    :return: Wrapper decorator
    """

    # TODO: Add some deeper documentation for this process
    # TODO: Cleanup all commented-out sections
    # TODO: Add decorator for authentication management
    # TODO: Verify this is best practice for wrapping decorators
    def decorator(f):
        """Wrapper decorator to save on useless verbosity"""
        # pylint: disable=unused-variable
        @JSONRPC.method(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            """Wrapper decorator to save on useless verbosity"""
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                rv = rv[0]
            return rv
        return f

    return decorator


def on_api_error(e):
    """ Custom error handler for general 400 errors.

    :param e: General error
    :type e: :class:`{{cookiecutter.repo_name}}.core.ComputeError`

    :return: Error message, 400
    :rtype: json, int
    """
    return jsonify(dict(error=e.msg)), 400


def on_api_form_error(e):
    """ Custom error handler for 400 form errors.

    :param e: Form error
    :type e: :class:`{{cookiecutter.repo_name}}.core.ComputeFormError`

    :return: Error message, 400
    :rtype: json, int
    """
    return jsonify(dict(errors=e.errors)), 400


def on_404(e):
    """ Custom error handler for 404 errors.

    :param e: Error
    :type e: :class:`Exception`

    :return: Error message, 404
    :rtype: json, int
    """
    # pylint: disable=unused-argument
    return jsonify(dict(error='Not found')), 404

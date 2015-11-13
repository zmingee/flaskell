# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.repo_name }}.api
    ################

    API sub-app package implemented via JSON-RPC
"""

from functools import wraps

from flask_jsonrpc.exceptions import Error

from .. import factory
from ..extensions import JSONRPC


def create_app(settings_override=None):
    """ Uses app factory to generate Flask app for blueprints in sub-app

    :param dict settings_override: Dictionary of settings to override

    :return: Flask sub-app for JSON-RPC API
    :rtype: :class:`flask.Flask`
    """

    app = factory.create_app(__name__, __path__, settings_override)

    return app


def route(*args, **kwargs):
    """ Wrapper decorator for ``@jsonrpc.method`` so we can chain multiple
    decorators together

    :param args: args to pass to decorator(s)
    :param kwargs: kwargs to pass to decorator(s)

    :return: Wrapper decorator
    """

    # TODO: Add decorator for authentication management
    def decorator(f):
        """Wrapper decorator to save on useless verbosity"""
        # pylint: disable=unused-variable
        @JSONRPC.method(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            """Run wrapped function"""
            rv = f(*args, **kwargs)
            return rv
        return f

    return decorator


# TODO: Determine best way to share errors and handlers between types of apps (frontend, REST, etc)

# class ComputeError(Error):
#     """Base application error class."""
#     status = 500
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


class {{ cookiecutter.repo_name|capitalize }}FormError(Error):
    """Raise when an error processing a form occurs."""
    status = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

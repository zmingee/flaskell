"""
API sub-app package implemented via JSON-RPC
"""

from .. import factory
from ..extensions import JSONRPC


def create_app(settings_override=None):
    """
    Uses app factory to generate Flask app for blueprints in sub-app

    :param dict settings_override: Dictionary of settings to override
    :return: Flask sub-app for JSON-RPC API
    :rtype: :class:`flask.Flask`
    """

    app = factory.create_app(__name__, __path__, settings_override)

    return app

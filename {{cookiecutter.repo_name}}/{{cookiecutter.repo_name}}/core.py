# -*- coding: utf-8 -*-
"""
    {{cookiecutter.repo_name}} core module containing things like application-wide
    errors
"""

from flask_jsonrpc.exceptions import Error

class {{cookiecutter.repo_name|capitalize}}Error(Error):
    """Base application error class."""
    status = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class {{cookiecutter.repo_name|capitalize}}FormError(Error):
    """Raise when an error processing a form occurs."""
    status = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

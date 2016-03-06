"""
Application-wide exceptions module
"""

from flask_jsonrpc.exceptions import Error


class {{cookiecutter.repo_name|capitalize}}Error(Error):
    """
    Raised when the called subsystem or service layer experiences a server-side error

    :Example:

    ::

        [JSON-RPC RESPONSE - TESTING CONDITIONS]
            {
                'jsonrpc': '2.0',
                'error': {
                    'code': 500,
                    'data': None,
                    'message': 'Failed',
                    'name': '{{cookiecutter.repo_name|capitalize}}Error',
                },
                'id': 0
            }

        [JSON-RPC RESPONSE - NORMAL CONDITIONS]
            {
                'jsonrpc': '2.0',
                'error': {
                    'code': 500,
                    'message': 'Failed',
                },
                'id': 0
            }

    """
    status = 500


class {{cookiecutter.repo_name|capitalize}}FormError(Error):
    """
    Raised when an error processing parameters passed to a JSON-RPC endpoint
    """
    status = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

"""
    tests.api
    #########

    api tests package
"""

from {{cookiecutter.repo_name}}.api import create_app

from .. import {{cookiecutter.repo_name|capitalize}}AppTestCase, settings

class {{cookiecutter.repo_name|capitalize}}ApiTestCase({{cookiecutter.repo_name|capitalize}}AppTestCase):
    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super({{cookiecutter.repo_name|capitalize}}ApiTestCase, self).setUp()

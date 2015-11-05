# -*- coding: utf-8 -*-
"""
    tests
    #####

    tests package
"""

from unittest import TestCase

from .utils import FlaskTestCaseMixin

# TODO: Add tests for service layer with a unit test approach
# TODO: Document approach for testing

class {{cookiecutter.repo_name|capitalize}}TestCase(TestCase):
    pass


class {{cookiecutter.repo_name|capitalize}}AppTestCase(FlaskTestCaseMixin, {{cookiecutter.repo_name|capitalize}}TestCase):

    def _create_app(self):
        raise NotImplementedError

    def _create_fixtures(self):
        pass

    def setUp(self):
        super({{cookiecutter.repo_name|capitalize}}AppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self._create_fixtures()

    def tearDown(self):
        super({{cookiecutter.repo_name|capitalize}}AppTestCase, self).tearDown()
        self.app_context.pop()

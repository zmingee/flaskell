"""
This {{cookiecutter.repo_name|capitalize}} utils module contains methods and functions
that are _not_ related to the MSTV (Model-Service-Template-View)
functionality of the application. Methods defined here are for
generic functionality of the controller itself, like where to
store data related to the installed application, how to format
dates, or how to create directories. Any thing above these
kinds of use cases should be defined in the Celery and/or
Service Layer of the application.
"""

# pylint: disable=too-few-public-methods

import os
import json
import uuid
import logging
import pprint
from functools import wraps

import requests
from flask import current_app, request

from .exceptions import {{cookiecutter.repo_name|capitalize}}Error, {{cookiecutter.repo_name|capitalize}}Error

LOGGER = logging.getLogger(__name__)


def make_dir(dir_path):
    """Function for making directories"""
    try:
        os.makedirs(dir_path, exist_ok=True)
        LOGGER.debug('Creating directory - %s', dir_path)
    except PermissionError as e:
        LOGGER.exception('Unable to create directory! - %s', dir_path)
        raise e


def attempt_token_auth(auth_header):
    """
    Asserts that the given auth_header matches the SECRET_KEY defined in the Flask app context

    :param str auth_header: Header payload stripped from the request
    """
    try:
        assert auth_header == 'Token {0}'.format(current_app.config['SECRET_KEY'])
    except AssertionError:
        raise PermissionError

def auth_token(func):
    """
    Decorator to place in a view-layer function. Will authenticate a token with the
    :class:`flask.request` context (using the headers)
    """
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        """
        Wrapper for decorated function
        """
        LOGGER.info('Received request from IP - %s', request.environ.get('REMOTE_ADDR'))
        try:
            attempt_token_auth(request.environ.get('HTTP_AUTHORIZATION'))
        except PermissionError:
            LOGGER.error('Authorization failed for token %s',
                         request.environ.get('HTTP_AUTHORIZATION'))
            raise {{cookiecutter.repo_name|capitalize}}Error('Authorization failed')
        else:
            LOGGER.info('Successfully authenticated token')
        return func(*args, **kwargs)
    return func_wrapper


class CerberusValidate(object):
    """
    Decorator to validate request parameters against a given Cerberus schema
    """

    def __init__(self, schema):
        self.schema = schema

    def __call__(self, func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            """
            Wrapper for decorated function
            """
            LOGGER.info('Validating params with `%s`', self.schema.__name__)
            LOGGER.debug('Params - \n--ARGS--\n%s\n--KWARGS--\n%s', args, kwargs)
            v = self.schema()
            if v.validate(kwargs):
                LOGGER.debug('Successfully validated params')
                return func(*args, **kwargs)
            else:
                LOGGER.error('Failed to validate params - \n%s', v.errors)
                raise {{cookiecutter.repo_name|capitalize}}Error(v.errors, 500)
        return func_wrapper

# -*- coding: utf-8 -*-
"""
    This {{cookiecutter.repo_name}} utils module contains methods and functions
    that are _not_ related to the MSTV (Model-Service-Template-View)
    functionality of the application. Methods defined here are for
    generic functionality of the controller itself, like where to
    store data related to the installed application, how to format
    dates, or how to create directories. Any thing above these
    kinds of use cases should be defined in the Celery and/or
    Service Layer of the application.
"""

import os

# from flask.json import JSONEncoder as BaseJSONEncoder

# TODO:: Move "INSTANCE_FOLDER_PATH" and various other configs to :module:`{{ cookiecutter.repo_name }}.config`

INSTANCE_FOLDER_PATH = os.path.join('/etc', '{{ cookiecutter.repo_name }}')


def make_dir(dir_path):
    """Function for making directories"""
    try:
        os.makedirs(dir_path, exist_ok=True)
    except Exception as e:
        raise e

# class JSONEncoder(BaseJSONEncoder):
#     """Custom :class:`JSONEncoder` which respects objects that include the
#     :class:`JsonSerializer` mixin.
#     """
#     # pylint: disable=method-hidden
#     def default(self, obj):
#         if isinstance(obj, JsonSerializer):
#             return obj.to_json()
#         return super(JSONEncoder, self).default(obj)


# class JsonSerializer(object):
#     """A mixin that can be used to mark a SQLAlchemy model class which
#     implements a :func:`to_json` method. The :func:`to_json` method is used
#     in conjuction with the custom :class:`JSONEncoder` class. By default this
#     mixin will assume all properties of the SQLAlchemy model are to be visible
#     in the JSON output. Extend this class to customize which properties are
#     public, hidden or modified before being being passed to the JSON serializer.
#     """
#
#     __json_public__ = None
#     __json_hidden__ = None
#     __json_modifiers__ = None
#
#     def get_field_names(self):
#         """Iterates through properties and yields out their keys"""
#         # pylint: disable=no-member
#         for class_props in self.__mapper__.iterate_properties:
#             yield class_props.key
#
#     def to_json(self):
#         """Converts to internal JSON structure"""
#         field_names = self.get_field_names()
#
#         public = self.__json_public__ or field_names
#         hidden = self.__json_hidden__ or []
#         modifiers = self.__json_modifiers__ or dict()
#
#         rv = dict()
#         for key in public:
#             rv[key] = getattr(self, key)
#         for key, modifier in modifiers.items():
#             value = getattr(self, key)
#             rv[key] = modifier(value, self)
#         for key in hidden:
#             rv.pop(key, None)
#         return rv

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

import string
import random
import os

from datetime import datetime

from flask.json import JSONEncoder as BaseJSONEncoder

# TODO:: Move "INSTANCE_FOLDER_PATH" and various other configs to :module:`{{cookiecutter.repo_name}}.config`

# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = os.path.join('/etc', '{{cookiecutter.repo_name}}')

ALLOWED_AVATAR_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Form validation

USERNAME_LEN_MIN = 4
USERNAME_LEN_MAX = 25

REALNAME_LEN_MIN = 4
REALNAME_LEN_MAX = 25

PASSWORD_LEN_MIN = 6
PASSWORD_LEN_MAX = 16

AGE_MIN = 1
AGE_MAX = 300

DEPOSIT_MIN = 0.00
DEPOSIT_MAX = 9999999999.99

# Sex type.
MALE = 1
FEMALE = 2
OTHER = 9
SEX_TYPE = {
    MALE: u'Male',
    FEMALE: u'Female',
    OTHER: u'Other',
}

# Model
STRING_LEN = 64


def get_current_time():
    """Method to return current time in UTC"""
    return datetime.utcnow()


def pretty_date(date, default=None):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    Ref: https://bitbucket.org/danjac/newsmeme/src/a281babb9ca3/newsmeme/
    """

    if default is None:
        default = 'just now'

    now = datetime.utcnow()
    diff = now - date

    periods = (
        (diff.days / 365, 'year', 'years'),
        (diff.days / 30, 'month', 'months'),
        (diff.days / 7, 'week', 'weeks'),
        (diff.days, 'day', 'days'),
        (diff.seconds / 3600, 'hour', 'hours'),
        (diff.seconds / 60, 'minute', 'minutes'),
        (diff.seconds, 'second', 'seconds'),
    )

    for period, singular, plural in periods:

        if not period:
            continue

        if period == 1:
            return u'%d %s ago' % (period, singular)
        else:
            return u'%d %s ago' % (period, plural)

    return default


def allowed_file(filename):
    """Definition of allowed files/types"""
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_AVATAR_EXTENSIONS


def id_generator(size=10, chars=string.ascii_letters + string.digits):
    """ID Generation"""
    #return base64.urlsafe_b64encode(os.urandom(size))
    return ''.join(random.choice(chars) for x in range(size))


def make_dir(dir_path):
    """Function for making directories"""
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except Exception as e:
        raise e

class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """
    # pylint: disable=method-hidden
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        """Iterates through properties and yields out their keys"""
        # pylint: disable=no-member
        for class_props in self.__mapper__.iterate_properties:
            yield class_props.key

    def to_json(self):
        """Converts to internal JSON structure"""
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv

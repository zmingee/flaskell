__author__ = 'dean.hutton'
# -*- coding: utf-8 -*-
"""
    Utils has nothing to do with models and views.
"""
import string
import random
import os
import time
# import iptools
# from pymongo import MongoClient
# from tasks import check_spam_ips
# import datetime
import collections
import uuid
from flask import current_app

# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')
def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception as e:
        raise e

def percentage(part, whole):
  return 100 * float(part)/float(whole)


def connect_to_mongodb():
    client = MongoClient('localhost', 27017)
    return client


def validateUUIDv4(uuID):
    try:
        job_id_uuid = uuid.UUID(uuID, version=4)
        job_id = str(job_id_uuid)
        return job_id
    except ValueError:
        return False
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint, current_app
from ..utils import start_spam_scan_celery_jobs
from ..extensions import jsonrpc
from ..utils import validate_input
from ..utils import connect_to_mongodb
from ..utils import percentage
from ..utils import convert_input_to_list
from ..utils import validateUUIDv4
import threading
import uuid
import datetime

api = Blueprint('api', __name__, url_prefix='/api')
keystone = 'http://os-controller.lab.corp.beyondhosting.net:5000/v2.0'
@jsonrpc.method('Security.index')
def index():
    return u'Welcome to the Security API'


@jsonrpc.method('Security.check_job_status(job_id=str)',validate=True)
def check_job_status(job_id):
    '''
    Return the status of a job to the user if it exists.

    :param str job_id: Job ID for job
    :return dict: Status of a job

    :Example:

    (Code call)
    instance.check_job_status(job_id="606a3523-7738-4e36-9153-0f01902b9d93")

    :Example:

    (JSON RPC)
    curl -i -X POST \
        -H "Content-Type: application/json; indent=4" \
        -d '{
            "jsonrpc": "2.0",
            "method": "Instance.check_job_status",
            "params": {
                 "job_id": "606a3523-7738-4e36-9153-0f01902b9d93",
            },
        }' \
        http://target/api
    '''
    #current_app.logger.info("Checking status %s",job_id)
    return {}

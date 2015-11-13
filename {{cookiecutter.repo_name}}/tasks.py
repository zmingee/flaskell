import os
import sys

from invoke import task, run

from setup import NAME, VERSION

@task
def setup_virtualenv():
    print('Creating virtualenv')
    run('virtualenv -p /usr/local/bin/python3 env',
        hide=True)
    activate_this = 'env/bin/activate_this.py'
    with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))
    run('pip install -r requirements.txt',
        hide=True)
    run('pip install -r devel-requirements.txt',
        hide=True)


@task(pre=[setup_virtualenv])
def run_debug():
    """
    Run in local machine.
    :return:
    """

    print('Running debug server')

    from werkzeug.serving import run_simple

    from {{ cookiecutter.repo_name }} import wsgi

    run_simple('0.0.0.0', 5000, wsgi.APPLICATION, use_reloader=True, use_debugger=True)


@task()
def tox():
    """
    Run tox
    :return:
    """

    print('Running tox')
    run('/usr/local/bin/tox --recreate')


@task()
def wheel():
    """
    Setup and upload wheel
    :return:
    """

    print('Building and uploading wheel')
    run('/usr/local/bin/python3 setup.py bdist_wheel upload -r local')

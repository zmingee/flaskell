import os
import sys
import multiprocessing as mp
import tempfile

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


def clean_up(x):
    return run('find . -name "{0}" | xargs rm -rf'.format(x))


@task
def clean():
    print('Cleaning directories')
    to_clean = (
        '*.pyc',
        '*.egg-info',
        '.coverage',
        '__pycache__',
        '.tox',
        'build',
        'dist',
    )

    #results = list(map((lambda x: run('find . -name "{0}" | xargs rm -rf'.format(x))), to_clean))

    pool = mp.Pool(processes=4)
    results = [pool.apply(clean_up, args=(x,)) for x in to_clean]


@task(pre=[setup_virtualenv])
def run_debug():
    """
    Run in local machine.
    :return:
    """

    print('Running debug server')

    from werkzeug.serving import run_simple

    from {{cookiecutter.repo_name}} import wsgi

    run_simple('0.0.0.0', 5000, wsgi.APPLICATION, use_reloader=True, use_debugger=True)


@task
def tox():
    """
    Run tox
    :return:
    """

    print('Running tox')
    run('/usr/local/bin/tox --recreate')

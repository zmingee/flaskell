import multiprocessing

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1
pid = '/srv/{{ cookiecutter.repo_name }}/gunicorn.pid'

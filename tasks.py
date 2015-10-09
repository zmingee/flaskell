from invoke import task, run
import sys

#from celery import Celery
# security_app = Celery('security-api')
# security_app.config_from_object('celeryconfig')

# @security_app.task(time_limit=2)#
# def check_spam_ips(ip,counter):
#     try:
#         resp = socket.gethostbyname(ip)
#     except:
#         resp = "none"
#
#     return {"response":resp,"ip":ip,"count":counter}


@task
def clean():
    """
    Clean up previous install

    :return:
    """

    print('Cleaning up old data and instance...')
    run('rm -rf /tmp/{{ name }}')
    run('mkdir /tmp/{{ name }}')

@task
def setup(pre=[clean]):
    """
    Setup virtual env.
    :return:
    """

    print('Starting build process')
    run("virtualenv -p python3 env")
    activate_this = "env/bin/activate_this.py"
    with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))
    run('python3 setup.py install')

@task
def run_debug():
    """
    Run in local machine.
    :return:
    """

    print("Running debug server")
    activate_this = "env/bin/activate_this.py"
    with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))
        print("virtualenv configured...")

    from {{ name }} import create_app
    app = create_app()
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    print("tasks.py is being run directly")
    print("http://localhost:5000/api/browse")
    if "run_debug" in sys.argv:
        run_debug()

    if "setup" in sys.argv:
        setup()
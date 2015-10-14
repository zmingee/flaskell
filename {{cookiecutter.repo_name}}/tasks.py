from invoke import task, run
from {{ name }} import create_app

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
    app = create_app()
    app.run(host='0.0.0.0')
import sys

from invoke import task, run

@task
def clean():
    """
    Clean up
    :return:
    """

    print('Removing virtualenv')
    run('rm -rf env')


@task
def setup_virtualenv():
    print('Creating virtualenv')
    run("virtualenv -p python3 env",
        hide=True)
    activate_this = "env/bin/activate_this.py"
    with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))
    run("pip install -r requirements.txt",
        hide=True)


@task(pre=[setup_virtualenv])
def pylint():
    """
    Check code using pylint
    :return:
    """

    print('Running pylint')
    rv = run('pylint {{cookiecutter.repo_name}} --good-names=rv,_,e,f,v --disable=wildcard-import,unused-wildcard-import,fixme',
             warn=True,
             hide=True)

    print("\n### START PYLINT OUTPUT ###")
    for l in rv.stdout.splitlines():
        print(">>> %s" % l)
    print("\n### END PYLINT OUTPUT ###")

    sys.exit(rv.exited)


@task(pre=[setup_virtualenv])
def sphinx():
    """
    Build Sphinx documentation
    :return:
    """

    print('Building sphinx docs')
    rv = run('sphinx-build -b html doc/source doc/_build',
             warn=True,
             hide=True)

    print("\n### START SPHINX-BUILD OUTPUT ###")
    for l in rv.stdout.splitlines():
        print(">>> %s" % l)
    print("\n### END SPHINX-BUILD ###")

    sys.exit(rv.exited)


@task(pre=[setup_virtualenv])
def nosetests_unit():
    """
    Run unit nosetests
    :return:
    """

    print('Running unit nosetests')
    run('cd tests')
    rv = run('nosetests -v -e integration -e functional 2>&1',
             warn=True,
             hide=True)

    print("\n### START NOSETESTS OUTPUT ###")
    for l in rv.stdout.splitlines():
        print(">>> %s" % l)
    print("\n### END NOSETESTS OUTPUT ###")

    sys.exit(rv.exited)



@task(pre=[setup_virtualenv])
def nosetests_functional():
    """
    Run functional nosetests
    :return:
    """

    print('Running functional nosetests')
    run('cd tests')
    rv = run('nosetests -v -e unit -e integration 2>&1',
             warn=True,
             hide=True)

    print("\n### START NOSETESTS OUTPUT ###")
    for l in rv.stdout.splitlines():
        print(">>> %s" % l)
    print("\n### END NOSETESTS OUTPUT ###")

    sys.exit(rv.exited)


@task(pre=[setup_virtualenv])
def nosetests_integration():
    """
    Run integration and coverage nosetests
    :return:
    """

    print('Running integration nosetests')
    run('cd tests')
    rv = run('nosetests -v --with-coverage --cover-package={{cookiecutter.repo_name}} 2>&1',
             warn=True,
             hide=True)

    print("\n### START NOSETESTS OUTPUT ###")
    for l in rv.stdout.splitlines():
        print(">>> %s" % l)
    print("\n### END NOSETESTS OUTPUT ###")

    sys.exit(rv.exited)


@task
def build_rpm():
    """
    Build RPM
    MUST BE RAN ON CENTOS/RHEL

    :return:
    """

    print("Building RPM...")
    run("mkdir /usr/local/bin/{{cookiecutter.repo_name}}")
    run("/usr/local/bin/virtualenv -p /usr/local/bin/python3 /usr/local/bin/{{cookiecutter.repo_name}}/env")
    run("/usr/local/bin/{{cookiecutter.repo_name}}/env/bin/pip3 install netifaces")
    run("/usr/local/bin/{{cookiecutter.repo_name}}/env/bin/python3 setup.py install")
    run("/usr/local/bin/fpm -s dir -t rpm -n {{cookiecutter.repo_name}} -v 0.5.0 -p {{cookiecutter.repo_name}}_VERSION_ARCH.rpm /usr/local/bin/{{cookiecutter.repo_name}}/=/usr/local/bin/{{cookiecutter.repo_name}}")


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

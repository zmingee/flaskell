include:
  - python3

gcc:
  pkg.installed:
    - refresh: True

/srv/{{ cookiecutter.repo_name }}:
  file.directory:
    - user: root
    - group: root
    - dir_mode: 755
    - file_mode: 644

/usr/local/bin/pip3 install virtualenv:
  cmd.run:
    - unless:
      - ls /usr/local/lib/python3.4/site-packages/virtualenv

/srv/{{ cookiecutter.repo_name }}/venv:
  virtualenv.managed:
    - system_site_packages: False
    - python: /usr/local/bin/python3
    - unless:
      - ls /srv/{{ cookiecutter.repo_name }}/venv

/srv/{{ cookiecutter.repo_name }}/gunicorn_conf.py:
  file.managed:
    - user: root
    - group: root
    - mode: 644
    - source: salt://{{ cookiecutter.repo_name }}-ms/gunicorn_conf.py

/srv/{{ cookiecutter.repo_name }}/venv/bin/pip install {{ cookiecutter.repo_name }}=={{ pillar['version'] }}:
  cmd.run: []

/etc/systemd/system/{{ cookiecutter.repo_name }}.service:
  file.managed:
    - user: root
    - group: root
    - mode: 644
    - source: salt://{{ cookiecutter.repo_name }}-ms/systemd.unit

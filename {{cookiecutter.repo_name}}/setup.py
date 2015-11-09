#!/usr/bin/env python3
from setuptools import setup
from pip.req import parse_requirements

version = '0.1.0'

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name={{cookiecutter.repo_name}},
    version=version,
    description={{cookiecutter.project_short_description}},
    license={{cookiecutter.license}},
    long_description={{cookiecutter.project_short_description}},
    author={{cookiecutter.full_name}},
    author_email={{cookiecutter.email}},
    url={{cookiecutter.project_url}},
    install_requires=reqs,
    packages=[
        {{cookiecutter.repo_name}},
    ],
    include_package_data=True,
    zip_safe=False,
)
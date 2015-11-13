#!/usr/bin/env python3
from setuptools import setup
from pip.req import parse_requirements

NAME = {{ cookiecutter.repo_name }}
VERSION = '0.1.0'


def main():
    setup(
        name=NAME,
        version=VERSION,
        description={{cookiecutter.project_short_description}},
        license={{cookiecutter.license}},
        long_description={{cookiecutter.project_short_description}},
        author={{cookiecutter.full_name}},
        author_email={{cookiecutter.email}},
        url={{cookiecutter.project_url}},
        install_requires=reqs,
        packages=[
            NAME,
        ],
        include_package_data=True,
        zip_safe=False,
    )

if __name__ == '__main__':
    INSTALL_REQS = parse_requirements('requirements.txt',
                                      session=False)
    REQS = [str(ir.req) for ir in INSTALL_REQS]

    main()

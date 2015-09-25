#!/usr/bin/env python3
from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name={{ name }}
    version={{ version }}
    description={{ description }}
    license={{ license }}
    long_description={{ long_description }}
    author={{ author }}
    author_email={{ author_email }}
    url={{ url }}
    install_requires=reqs,
    packages=[
        {{ name }},
    ],
    include_package_data=True,
    zip_safe=False,
    #entry_points={
    #    'console_scripts': [
    #
    #    ],
    #},
)
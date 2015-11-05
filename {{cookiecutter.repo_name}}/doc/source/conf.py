#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import alabaster

sys.path.append(os.path.abspath('../..'))

# Regular settings
master_doc = 'index'
project = '{{cookiecutter.repo_name}}'
copyright = '2015 {{cookiecutter.full_name}}'
author = '{{cookiecutter.full_name}}'
version = '0.1.0'
release = '0.1.0'
templates_path = ['_templates']
exclude_trees = ['_build']
exclude_patterns = []
source_suffix = '.rst'
pygments_style = 'sphinx'

# Extension Settings
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'alabaster',
]
intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://flask.pocoo.org/docs/0.10/': None}
autodoc_default_flags = ['members', 'special-members']
todo_include_todos = True

# Themeing
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
html_static_path = ['_static']
htmlhelp_basename = '{{cookiecutter.repo_name}}doc'
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

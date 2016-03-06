import sys
import os
from datetime import datetime

import alabaster

sys.path.append(os.path.abspath('..'))

from setup import VERSION

###########################################
### MONKEY PATCH FOR NONLOCAL IMAGE URI ###
import sphinx.environment
from docutils.utils import get_source_line

def _warn_node(self, msg, node):
    if not msg.startswith('nonlocal image URI found:'):
        self._warnfunc(msg, '%s:%s' % get_source_line(node))

sphinx.environment.BuildEnvironment.warn_node = _warn_node
### END MONKEY PATCH ###
########################

# Regular settings
master_doc = 'index'
project = '{{cookiecutter.repo_name|capitalize}}'
year = datetime.now().year
copyright = '{0}, {{cookiecutter.full_name}}'.format(year)
author = '{{cookiecutter.full_name}}'
version = VERSION
release = VERSION
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
    'releases'
]
intersphinx_mapping = {
    'http://docs.python.org/': None,
    'http://flask.pocoo.org/docs/0.10/': None,
    'http://werkzeug.pocoo.org/docs/0.11/': None,
}
autodoc_default_flags = ['members', 'special-members']
todo_include_todos = True

# Releases settings
releases_issue_uri = None
releases_release_uri = None

# Themeing
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
htmlhelp_basename = '{{cookiecutter.repo_name}}doc'
html_theme_options = {
    'github_button': False,
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

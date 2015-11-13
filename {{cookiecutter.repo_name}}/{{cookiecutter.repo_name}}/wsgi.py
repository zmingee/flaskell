# -*- coding: utf-8 -*-
"""
    wsgi
    ####

This module provides an entrypoint for WSGI servers, accessible by ``application``
or by running this file as a script.

This module is not currently using the :class:`werkzeug.wsgi.DispatcherMiddleware`
as there is not a need for it in this case. There is only one "app",
:module:`{{cookiecutter.repo_name}}.api`, so there is no need to have the functionality for
more to be added. This can be changed easily by using the commented-out sections
of this module.
"""

from werkzeug.serving import run_simple
#from werkzeug.wsgi import DispatcherMiddleware

from {{ cookiecutter.repo_name }} import api

#application = DispatcherMiddleware(frontend.create_app(), {
#    '/api': api.create_app()
#})

APPLICATION = api.create_app()

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, APPLICATION, use_reloader=True, use_debugger=True)

import os
import sys

from django.conf import settings


def get_cgi_handler_code():
    template = """#!{}
import wsgiref.handlers

from {} import {}

wsgiref.handlers.CGIHandler().run(application)
"""
    python = os.path.join(sys.prefix, 'bin', 'python')
    split = settings.WSGI_APPLICATION.split('.')
    module = '.'.join(split[:-1])
    application = split[-1]
    return template.format(python, module, application)

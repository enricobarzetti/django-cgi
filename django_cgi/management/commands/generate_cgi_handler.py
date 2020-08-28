import os

from django.core.management.base import BaseCommand

from django_cgi import get_cgi_handler_code


class Command(BaseCommand):
    help = 'Generate a CGI script'
    requires_system_checks = False

    def handle(self, *args, **options):
        path = 'cgi_handler.py'
        with open(path, 'w') as f:
            f.write(get_cgi_handler_code())
        os.chmod(path, 0o755)

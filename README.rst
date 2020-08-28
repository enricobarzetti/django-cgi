django-cgi
==========

Run Django with CGI

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-cgi

Install the app

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'django_cgi',
    )

Usage
-----

generate_cgi_handler command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    python manage.py generate_cgi_handler

This will create a file called cgi_handler.py next to manage.py.

Server config
-------------

Point your server to serve the cgi_handler.py file.  This is an example config for Apache:

.. code-block::

    LoadModule cgid_module lib/httpd/modules/mod_cgid.so
    ScriptAlias /path "/repo/cgi_handler.py"
    <Directory "/repo">
        AllowOverride None
        Options None
        Require all granted
    </Directory>

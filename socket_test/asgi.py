"""
ASGI config for socket_test project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os, django

from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socket_test.settings")

django.setup()

application = get_default_application()
``
"""
WSGI config for free_code_camp_tutorial_cfe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "free_code_camp_tutorial_cfe.settings")

application = get_wsgi_application()

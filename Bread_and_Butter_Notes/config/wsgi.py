"""
WSGI config for Bread_and_Butter_Notes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

print('Jim note: In wsgi.py line 16 may be a problem later. See "Preliminaries - Testing the Website."')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bread_and_Butter_Notes.settings")

application = get_wsgi_application()

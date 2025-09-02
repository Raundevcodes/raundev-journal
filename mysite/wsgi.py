"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# Define BASE_DIR manually
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Wrap with WhiteNoise to serve static files
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
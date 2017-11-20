import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_tango.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    
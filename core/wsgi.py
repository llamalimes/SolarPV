import os
import sys
sys.path.append('/home/bitnami/SolarPV')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/SolarPV/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fikrlar_va_takliflar_tizimi.settings')
application = get_wsgi_application()

import os
from celery import Celery
from . import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_rest_jwt.settings")

celery = Celery("django_rest_jwt")
celery.config_from_object("django.conf.settings",namespace="CELERY")
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
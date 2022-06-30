import os

from celery import Celery
from django.conf import settings


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "coingecko.settings"
)

app = Celery('coingecko')
app.config_from_object(settings, namespace="CELERY")

app.conf.beat_schedule = {
    "get_coins_data_every_minute": {
        "task": "cryptocurrencies.tasks.get_coins_data",
        "schedule": 60.0
    }
}

app.autodiscover_tasks()

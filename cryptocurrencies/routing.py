from django.urls import path

from .consumers import CryptocurrenciesConsumer

websocket_urlpatterns = [
    path("ws/cryptocurrencies", CryptocurrenciesConsumer.as_asgi())
]

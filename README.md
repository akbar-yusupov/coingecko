# Description
Real time updatable top cryptocurrencies list via Celery + Django Channels + CoinGecko API
# How to launch the project
Create database:
```
  python3 manage.py makemigrations
```
Run project:
```
  python3 manage.py runserver
  celery -A coingecko.celery worker --pool=solo -l info
  celery -A coingecko beat -l INFO
```

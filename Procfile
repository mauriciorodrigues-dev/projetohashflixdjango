release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn hashflix.wsgi:application --log-file -


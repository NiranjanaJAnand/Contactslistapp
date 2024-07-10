release: python manage.py makemigations --no-input
release: python manage.py migrate --no-input

web: gunicorn contactsapi.wsgi

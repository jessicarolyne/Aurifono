release: python3 aurifono/manage.py migrate
web: gunicorn --pythonpath aurifono aurifono.wsgi --preload --log-file –
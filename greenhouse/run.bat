@ECHO OFF
start python manage.py runserver
start celery -A greenhouse worker --pool=solo -l info
start celery -A greenhouse beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
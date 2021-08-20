import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('Wysłanie maila!'), name='add every 10')


@app.task
def test(argument):
    print(f'{argument}')



app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#celery -A mysite worker -l info --pool=solo

#celery -A mysite beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
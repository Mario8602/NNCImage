import os
import time

from celery import Celery
from dotenv import load_dotenv
from django.conf import settings
from django.core.mail import send_mail


load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = settings.CELERY_BROKER_URL

app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(10)
    print('HELLO FROM CELERY')


@app.task()
def send_subscription():
    subject = 'Подписка на рассылку'
    message = 'Вы успешно подписались на рассылку'
    from_email = os.getenv('FROM_EMAIL')
    to_email = os.getenv('TO_EMAIL')
    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False
        )

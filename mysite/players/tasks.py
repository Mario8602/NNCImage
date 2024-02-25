import os

from dotenv import load_dotenv
from django.core.mail import send_mail

from mysite import celery


load_dotenv()


@celery.app.task()
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

from django.core.mail import send_mail

# from celery import shared_task
# from mysite.mysite.celery import app
from mysite import celery


# @shared_task
# def send_subscription():
#     subject = 'Подписка на рассылку'
#     message = 'Вы успешно подписались на рассылку'
#     from_email = 'hellp8901@gmail.com'
#     to_email = 'hellp8901@yandex.ru'
#     return send_mail(subject, message, from_email, [to_email])


@celery.app.task()
def send_subscription():
    subject = 'Подписка на рассылку'
    message = 'Вы успешно подписались на рассылку'
    from_email = 'hellp8901@gmail.com'
    to_email = 'hellp8901@yandex.ru'
    send_mail(
        subject, 
        message, 
        from_email, 
        [to_email]
        )
from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Subscriptions


@shared_task
def user_send_mail(course_id):
    """ Асинхронная рассылка писем пользователям об обновлении материалов курса """
    course_subscriptions = Subscriptions.objects.filter(course=course_id)
    for subscription in course_subscriptions:
        send_mail(
            subject="Обновление материалов курса",
            message=f'Курс {subscription.course.name} был обновлен.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False
        )

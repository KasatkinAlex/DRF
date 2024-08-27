import datetime

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def user_deactivate():
    """ если пользователь не заходил более месяца, блокирует его с помощью флага is_active"""
    today = timezone.now().today().date()
    users = User.objects.all()
    for user in users:
        if user.last_login is not None:
            time = today - user.last_login.date()
            if time > datetime.timedelta(weeks=4):
                user.is_staff = False

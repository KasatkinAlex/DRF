from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='akasatkin1990@mail.ru',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345')
        user.save()

        user1 = User.objects.create(
            email='test@mail.ru',
            first_name='Admin',
            last_name='Admin',
            is_staff=False,
            is_superuser=False
        )

        user1.set_password('12345')
        user1.save()

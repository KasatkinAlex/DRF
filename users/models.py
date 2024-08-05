from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Courses, Lesson


class User(AbstractUser):
    username = None

    avatar = models.ImageField(upload_to='avatar_user/', verbose_name='аватар', help_text='загрузите Ваше фото',
                               null=True, blank=True, )
    phone = models.CharField(max_length=30, verbose_name='телефон', null=True, blank=True)
    country = models.CharField(max_length=30, verbose_name='страна', null=True, blank=True)

    email = models.EmailField(max_length=100, unique=True, verbose_name='почта')

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class UserPayment(models.Model):
    CASH = 'Наличные'
    TRANSFER = 'Перевод на счет'

    PAYMENT_METHOD = [
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user')
    date_payment = models.DateField(verbose_name='Дата оплаты')
    course_paid = models.ManyToManyField(Courses, verbose_name='выберите курс',
                                         blank=True, related_name='user_payment_course')
    lesson_paid = models.ManyToManyField(Lesson, verbose_name='выберите урок',
                                         blank=True, related_name='user_payment_lesson')
    amount = models.FloatField(verbose_name='сумма оплаты')
    method = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Платежи'
        verbose_name_plural = 'Платежи'
        ordering = ['user']

from django.db import models

from config.settings import AUTH_USER_MODEL


class Courses(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', help_text='введите название')
    image = models.ImageField(upload_to='course_image/', verbose_name='Изображение', null=True, blank=True,
                                      help_text='Загрузите изображение курса')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание курса', null=True, blank=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name']  # Сортировка


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', help_text='введите название урока')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание урока', null=True, blank=True)
    image = models.ImageField(upload_to='lesson_image/', verbose_name='Изображение', null=True, blank=True,
                              help_text='Загрузите изображение урока')
    video = models.CharField(max_length=150, verbose_name='ссылка на видео',
                             help_text='вставте ссылку на видео', null=True, blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, verbose_name='выберите курс',
                                null=True, blank=True, related_name='lesson')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name']

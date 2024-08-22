from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Courses, Subscriptions
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='akasatkin1990@mail.ru')
        self.courses = Courses.objects.create(name='test1', owner=self.user)
        self.lesson = Lesson.objects.create(name='test', description='test', owner=self.user, courses=self.courses)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            'name': "test2"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            'name': "test99"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), "test99"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        print(response.json())
        data = {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': self.lesson.pk, 'name': self.lesson.name, 'description': self.lesson.description, 'image': None,
             'video': None,
             'courses': self.courses.pk, 'owner': self.user.pk}]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)
        self.assertEqual(response.json(), data)

    class SubscriptionsTestCase(APITestCase):
        def setUp(self) -> None:
            self.url = reverse("courses:subscription_create")
            user = {
                "email": "test@test.mail.ru",
                "first_name": "test",
                "last_name": "test",
                "is_staff": True,
                "is_superuser": True,
            }
            self.test_user = User.objects.create(**user)
            self.test_user.set_password("12345678")
            self.client.force_authenticate(user=self.test_user)
            self.test_course = Courses.objects.create(name="test")

        def test_sub_activate(self):
            """Тест подписки на курс"""
            data = {
                "user": self.test_user.id,
                "course": self.test_course.id,
            }
            response = self.client.post(self.url, data=data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(
                response.json(),
                {
                    "message": "Подписка добавлена",
                },
            )
            self.assertTrue(
                Subscriptions.objects.all().exists(),
            )

        def test_sub_deactivate(self):
            """Тест отписки с курса"""
            Subscriptions.objects.create(user=self.test_user, course=self.test_course)
            data = {
                "user": self.test_user.id,
                "course": self.test_course.id,
            }
            response = self.client.post(self.url, data=data)
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK,
            )
            self.assertEqual(
                response.json(),
                {
                    "message": "Подписка удалена",
                },
            )
            self.assertFalse(
                Subscriptions.objects.all().exists(),
            )

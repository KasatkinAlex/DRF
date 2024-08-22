from rest_framework import viewsets, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Courses, Lesson, Subscriptions
from materials.paginators import MyPagination
from materials.serializers import CoursesSerializer, LessonSerializer, CoursesDetailSerializer, SubscriptionSerializer
from users.permissions import IsModer, IsOwner


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    pagination_class = MyPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':  # действие == "просмотр"
            return CoursesDetailSerializer
        return CoursesSerializer

    def perform_create(self, serializer):
        """Автоматическое присвоение владельца уроку"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer, )
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner, )  # знак | означает или
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner, )
        return super().get_permissions()


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = MyPagination


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)  # не менеджер

    def perform_create(self, serializer):
        """Автоматическое присвоение владельца уроку"""
        serializer.save(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Детальная информация."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,  IsOwner | ~IsModer)


class SubscriptionAPIView(APIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course')
        course_item = get_object_or_404(Courses, id=course_id)
        subs_item = Subscriptions.objects.filter(user=user, course=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscriptions.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'
        return Response({"message": message})


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscriptions.objects.all()

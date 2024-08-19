from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Courses, Lesson
from materials.serializers import CoursesSerializer, LessonSerializer, CoursesDetailSerializer
from users.permissions import IsModer, IsOwner


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()

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
    permission_classes = (IsAuthenticated,  IsOwner, ~IsModer)

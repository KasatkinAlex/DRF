from rest_framework import viewsets, generics

from materials.models import Courses, Lesson
from materials.serializers import CoursesSerializer, LessonSerializer, CoursesDetailSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':  # действие == "просмотр"
            return CoursesDetailSerializer
        return CoursesSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
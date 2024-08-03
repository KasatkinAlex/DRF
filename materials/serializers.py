from rest_framework import serializers

from materials.models import Courses, Lesson


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


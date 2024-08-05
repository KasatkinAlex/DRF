from rest_framework import serializers

from materials.models import Courses, Lesson


class CoursesSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(source='lesson')

    class Meta:
        model = Courses
        fields = ('name', 'image', 'description', 'lesson_count')

    def get_lesson_count(self, instance):
        return instance.lesson.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


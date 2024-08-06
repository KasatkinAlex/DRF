from rest_framework import serializers

from materials.models import Courses, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CoursesDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(source='lesson')
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = ('name', 'image', 'description', 'lesson_count', 'lesson')

    def get_lesson_count(self, instance):
        return instance.lesson.count()


class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'


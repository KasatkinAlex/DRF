from rest_framework import serializers

from materials.models import Courses, Lesson, Subscriptions
from materials.validators import OtherResourcesValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            OtherResourcesValidator(field='name'),
            OtherResourcesValidator(field='description'),
            OtherResourcesValidator(field='video')
                      ]


class CoursesDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(source='lesson')
    lesson = LessonSerializer(many=True, read_only=True)
    is_subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Courses
        fields = ('name', 'image', 'description', 'lesson_count', 'lesson', 'is_subscription')

    def get_lesson_count(self, instance):
        return instance.lesson.count()

    def get_is_subscription(self, instance):
        return Subscriptions.objects.filter(user=self.context['request'].user, course=instance.pk).exists()


class CoursesSerializer(serializers.ModelSerializer):
    is_subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Courses
        fields = '__all__'
        validators = [
            OtherResourcesValidator(field='name'),
            OtherResourcesValidator(field='description')
        ]

    def get_is_subscription(self, instance):
        return Subscriptions.objects.filter(user=self.context['request'].user, course=instance.pk).exists()


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = '__all__'

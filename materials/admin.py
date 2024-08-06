from django.contrib import admin

from materials.models import Courses, Lesson


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'video', 'courses')
    search_fields = ('name', 'courses',)

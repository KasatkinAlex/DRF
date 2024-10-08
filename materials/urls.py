from django.urls import path, include
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CoursesViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView, SubscriptionAPIView, SubscriptionListAPIView

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r'courses', CoursesViewSet)
# router.register("subscription", SubscriptionAPIView, basename="subscription")

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('subscription/create/', SubscriptionAPIView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list')

] + router.urls

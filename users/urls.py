from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UserPaymentViewSet, UserPaymentListView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r'userpayment', UserPaymentViewSet)

urlpatterns = [
    path('payment/', UserPaymentListView.as_view(), name='userpayment_list'),
    # path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    # path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    # path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    # path('lesson/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson_delete')

] + router.urls

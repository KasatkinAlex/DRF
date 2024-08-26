from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserPaymentViewSet, UserPaymentListView, UserCreateAPIView, UserPaymentsCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r'userpayment', UserPaymentViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('payment/', UserPaymentListView.as_view(), name='userpayment_list'),
    path('payment/create/', UserPaymentsCreateAPIView.as_view(), name='userpayment_create'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    # path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    # path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    # path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    # path('lesson/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson_delete')

] + router.urls

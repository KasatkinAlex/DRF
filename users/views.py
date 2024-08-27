from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import UserPayment, User
from users.serializer import UserPaymentSerializer, UserSerializer, UserSerializerList
from users.services import create_stripe_product, create_stripe_price, create_stripe_session


class UserPaymentViewSet(viewsets.ModelViewSet):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['course_paid', 'lesson_paid', 'method', 'user']
    ordering_fields = ['date_payment',]


class UserPaymentListView(ListAPIView):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer
     # Бэкенд для обработки фильтра
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ('amount', 'user', 'lesson_paid', 'course_paid')  # Набор полей для фильтрации
    ordering_fields = ['date_payment',]


class UserPaymentsCreateAPIView(CreateAPIView):
    """Создание платежа"""
    serializer_class = UserPaymentSerializer
    queryset = UserPayment.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        payments = serializer.save()
        payments.user = self.request.user
        stripe_product_id = create_stripe_product(payments)
        price = create_stripe_price(stripe_product_id=stripe_product_id, amount=payments.amount)
        session_id, payment_link = create_stripe_session(price=price)
        payments.session_id = session_id
        payments.link = payment_link
        payments.save()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerList


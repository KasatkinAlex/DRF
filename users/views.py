from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import UserPayment, User
from users.serializer import UserPaymentSerializer, UserSerializer


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


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

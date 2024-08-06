from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.generics import ListAPIView

from users.models import UserPayment
from users.serializer import UserPaymentSerializer


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

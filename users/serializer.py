from rest_framework import serializers
from rest_framework.views import APIView

from users.models import UserPayment, User


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment_list = UserPaymentSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'

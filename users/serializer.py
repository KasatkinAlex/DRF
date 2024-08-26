from rest_framework import serializers
from rest_framework.views import APIView

from users.models import UserPayment, User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = '__all__'


class UserSerializerList(serializers.ModelSerializer):
    payment_list = UserPaymentSerializer(source="user", many=True)   # source="user" это взяли из описании модели related_name

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "payment_list")

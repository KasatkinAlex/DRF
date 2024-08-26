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
    # payment_list = serializers.SerializerMethodField(read_only=True)
    payment = UserPaymentSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'payment')

    # def get_payment_list(self, instance):
    #     return instance.payment.count()





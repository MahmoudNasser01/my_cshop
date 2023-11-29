
from dj_rest_auth.models import TokenModel

from rest_framework import serializers

from .models import Driver,Seller,Workshop,Customer,User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email')  # Add any additional fields you want to include

class CustomTokenSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Include the custom user serializer

    class Meta:
        model = TokenModel
        fields = ('key', 'user')


def create_serializer(model):
    self=model
    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = self
            fields = '__all__'
    return DynamicSerializer



DriverSerializer = create_serializer(Driver)
SellerSerializer = create_serializer(Seller)
WorkshopSerializer = create_serializer(Workshop)
CustomerSerializer = create_serializer(Customer)
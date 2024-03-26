
from dj_rest_auth.models import TokenModel
from dj_rest_auth.serializers import LoginSerializer

from rest_framework import serializers

from .models import Driver,Seller,Workshop,Customer,User,WorkshopMore,DriverMore,SellerMore


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
            fields = ['phone_number', 'name', 'username', 'is_staff','password','is_superuser']
    return DynamicSerializer




class CustomLoginSerializer(LoginSerializer):


    email = None
DriverSerializer = create_serializer(Driver)
SellerSerializer = create_serializer(Seller)
WorkshopSerializer = create_serializer(Workshop)
CustomerSerializer = create_serializer(Customer)

#for class more all
class DriverMoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverMore
        fields = ['address','user','phone','name']

class SellerMoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerMore
        fields = ['address','user','car','phone','name']

class WorkshopMoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopMore
        fields = ['address','user','cartypes','phone','name']

# this for reutrn dreiver and seller and workshop for delevery serlizer
class DriverMoreSerializer_dilvery(serializers.ModelSerializer):
    class Meta:
        model = DriverMore
        fields = ['address','user','phone','name']

class SellerMoreSerializer_dilvery(serializers.ModelSerializer):
    class Meta:
        model = SellerMore
        fields = ['name']

class WorkshopMoreSerializer_dilvery(serializers.ModelSerializer):
    class Meta:
        model = WorkshopMore
        fields = ['address','phone','name']

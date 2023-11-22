from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Driver,Seller,Workshop,Customer

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
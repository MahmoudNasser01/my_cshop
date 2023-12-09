from rest_framework import serializers

from .models import CountryCar, CompanyCar, carmodel, \
    CarName, Products, Sections, Order, Delivery


def meta(self):
    class Meta:
        model = self
        fields = '__all__'

    return Meta
class CountrySerializer(serializers.ModelSerializer):
    Meta = meta(CountryCar)

class ManufacturerSerializer(serializers.ModelSerializer):
    Meta = meta(CompanyCar)

class CarModelSerializer(serializers.ModelSerializer):
    Meta = meta(carmodel)

class CarDetailsSerializer(serializers.ModelSerializer):
    Meta = meta(CarName)

class SectionSerializer(serializers.ModelSerializer):
    Meta = meta(Sections)
class ProductSerializer(serializers.ModelSerializer):
    Meta = meta(Products)


#---

class AddToBasketSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class BasketItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()  # Update the source to match the key in the input data
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()

class BasketSummarySerializer(serializers.Serializer):
    items = BasketItemSerializer(many=True)
    total_quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id','user', 'product','total_price', 'quantity']


class DeliverySerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True,read_only=True)  # Nested OrderSerializer

    class Meta:
        model = Delivery
        fields = ['id', 'delivery_type', 'user', 'name', 'phone', 'orders']


class DeliverySerializer_write(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['id', 'delivery_type', 'user', 'name', 'phone', 'orders']


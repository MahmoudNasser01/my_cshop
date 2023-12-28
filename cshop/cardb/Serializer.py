from rest_framework import serializers

from .models import CountryCar, CompanyCar, carmodel, \
    CarName, Products, Sections, Order, Delivery,add_delvery
from users.models import User

def meta(self):
    class Meta:
        model = self
        fields = '__all__'

    return Meta
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
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


    class Meta:
        model = Products
        fields = '__all__'


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
#-----
class OrderSerializer_read(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    product = ProductSerializer(read_only=True)
    Meta = meta(Order)

class OrderSerializer(serializers.ModelSerializer):

    total_price = serializers.ReadOnlyField()
    Meta = meta(Order)


class DeliverySerializer(serializers.ModelSerializer):
    orders = OrderSerializer_read(many=True,read_only=True)  # Nested OrderSerializer

    class Meta:
        model = Delivery
        fields = ['order_bollen','id', 'delivery_type','status','name', 'phone','address', 'orders','location']


class DeliverySerializer_write(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['id', 'delivery_type','name', 'phone','address', 'orders','location']


class DeliverySerializer_workshop(serializers.ModelSerializer):
    orders = OrderSerializer(many=True,read_only=True)
    name=serializers.CharField(read_only=True)
    phone=serializers.CharField(read_only=True)
    address=serializers.CharField(read_only=True)
    delivery_type=serializers.CharField(read_only=True)
    class Meta:
        model = Delivery
        fields = ['order_bollen', 'delivery_type','name', 'phone','address', 'orders']



##in this i will create a serializer for add delvery and what i need so i will creat some serlizer like up
class ProductSerializer_driver(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['name', 'price','user',]

class Delivery_driver(serializers.ModelSerializer):
    orders = OrderSerializer_read(many=True,read_only=True)  # Nested OrderSerializer

    class Meta:
        model = Delivery
        fields = ['order_bollen','id', 'delivery_type','status','name', 'phone','address', 'orders','location']


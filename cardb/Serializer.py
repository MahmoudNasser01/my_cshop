from rest_framework import serializers

from .models import CountryCar, CompanyCar, carmodel, \
    CarName, Products, Sections, Order, Delivery,add_delvery
from users.models import User, WorkshopMore, DriverMore, SellerMore

from users.Serializer import WorkshopMoreSerializer, DriverMoreSerializer, SellerMoreSerializer,\
    SellerMoreSerializer_dilvery, WorkshopMoreSerializer_dilvery, DriverMoreSerializer_dilvery



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
    user = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['section', 'user', 'name', 'image', 'is_available', 'created_at', 'price', 'year','user_specific_id']

    def get_user(self, obj):
        return obj.user.name if obj.user else None


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
    user = serializers.SerializerMethodField()
    total_price = serializers.ReadOnlyField()

    Meta = meta(Order)
    def get_user(self, obj):
        return obj.user.name if obj.user else None

class OrderSerializer(serializers.ModelSerializer):

    total_price = serializers.ReadOnlyField()
    Meta = meta(Order)




class DeliverySerializer(serializers.ModelSerializer):
    orders = OrderSerializer_read(many=True,read_only=True)  # Nested OrderSerializer

    class Meta:
        model = Delivery
        fields = ['order_bollen', 'delivery_type','address', 'orders']


class DeliverySerializer_write(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['delivery_type','address', 'orders']


class DeliverySerializer_workshop(serializers.ModelSerializer):
    orders = OrderSerializer(many=True,read_only=True)

    address=serializers.CharField(read_only=True)
    delivery_type=serializers.CharField(read_only=True)
    class Meta:
        model = Delivery
        fields = ['order_bollen', 'delivery_type','address', 'orders']



##in this i will create a serializer for add delvery and what i need so i will creat some serlizer like up
class ProductSerializer_driver(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['name', 'price']

        def get_user(self, obj):
            return obj.user.name if obj.user else None


class OrderSerializer_driver(serializers.ModelSerializer):

    total_price = serializers.ReadOnlyField()
    product = ProductSerializer_driver(read_only=True)


    class Meta:
        model = Order
        fields = ['product','quantity', 'total_price']  # Include 'id' and 'user' if needed



class Delivery_driver_read(serializers.ModelSerializer):
    orders = OrderSerializer_driver(many=True,read_only=True)
    address=serializers.CharField(read_only=True)
    selermore=SellerMoreSerializer_dilvery(read_only=True)
    workshop=WorkshopMoreSerializer_dilvery(read_only=True)
    total_price = serializers.SerializerMethodField()  # Use SerializerMethodField to define custom methods

    class Meta:
        model = Delivery
        fields = ['phone','address', 'orders', 'workshop', 'selermore',
                  'total_price']

    def get_total_price(self, obj):
        total_price = 0
        for order in obj.orders.all():
            total_price += order.total_price
        return total_price


class Delivery_driver(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['order_bollen','delivery_type','address', 'orders','workshop','selermore','id']



class AddDelivery_driver_read(serializers.ModelSerializer):
    delivery = Delivery_driver_read(read_only=True)

    Meta = meta(add_delvery)
class AddDelivery_driver(serializers.ModelSerializer):
    class Meta:
        model = add_delvery
        fields = ['user','delivery']



class AddDelivery_driver_status(serializers.ModelSerializer):

    class Meta:
        model = add_delvery
        fields = ['user','delivery','status']
        extra_kwargs = {
            'status': {'default': 'pending'}  # Set the default value for the status field
        }

    def save(self, **kwargs):
        # Set the user field to request.user
        self.validated_data['user'] = self.context['request'].user
        return super().save(**kwargs)







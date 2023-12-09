# Create your views here.
from django.contrib.gis.geos import Point
from geopy import Nominatim
from rest_framework import generics, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CountryCar, CompanyCar, Order, carmodel, CarName, Sections, Products, Delivery
from .Serializer import CarDetailsSerializer, CarModelSerializer, CountrySerializer, ManufacturerSerializer, \
    SectionSerializer,DeliverySerializer_write,\
    ProductSerializer, OrderSerializer, DeliverySerializer


class IsSellerUser(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        # Check if the user is authenticated and is of type 'SELLER'
        return request.user.is_authenticated and request.user.type == 'SELLER'

class IsWorkShopUser(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        # Check if the user is authenticated and is of type 'WORKSHOP'
        return request.user.is_authenticated and request.user.type == 'WORKSHOP'


class CountryListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = CountryCar.objects.all()
    serializer_class = CountrySerializer



class ManufacturerListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyCar.objects.all()
    serializer_class = ManufacturerSerializer



class CarModelListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset =carmodel.objects.all()
    serializer_class = CarModelSerializer

   #------------------
class CarDetailsListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]
    queryset = CarName.objects.all()
    serializer_class = CarDetailsSerializer

class CarDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]
    queryset = CarName.objects.all()
    serializer_class = CarDetailsSerializer


#-------
class SectionListCreateView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]  # Only allows seller users
    queryset = Sections.objects.all()
    serializer_class = SectionSerializer

class SectionListCreateViewworkshop(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsWorkShopUser]  # Only allows workshop users
    queryset = Sections.objects.all()

    def get_queryset(self):
        return Sections.objects.filter(user=self.request.user)

    serializer_class = SectionSerializer

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsWorkShopUser]  # Only allows workshop users
    queryset = Sections.objects.all()

    def get_queryset(self):
        return Sections.objects.filter(user=self.request.user)

    serializer_class = SectionSerializer

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]  # Only allows seller users
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateViewwork(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsWorkShopUser]  # Only allows workshop users
    queryset = Products.objects.all()

    def get_queryset(self):
        return Products.objects.filter(user=self.request.user)

    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsWorkShopUser]  # Only allows workshop users
    queryset = Products.objects.all()

    def get_queryset(self):
        return Products.objects.filter(user=self.request.user)

    serializer_class = ProductSerializer


# ordrer
class OrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]  # Only allows seller users
    queryset = Order.objects.all()

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


    serializer_class = OrderSerializer
    def perform_create(self, serializer):
        # Set the user to the currently authenticated user before saving the order
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]  # Only allows seller users
    queryset = Order.objects.all()
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    serializer_class = OrderSerializer

#delvery
geolocator = Nominatim(user_agent="location")
class DeliveryListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]
    queryset = Delivery.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            # Use OrderCreateSerializer for POST requests (creation)
            return DeliverySerializer_write
        else:
            # Use OrderListSerializer for GET requests (listing)
            return DeliverySerializer














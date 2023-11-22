# Create your views here.
from rest_framework import generics, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CountryCar, CompanyCar, carmodel, CarName, Sections,Products
from .Serializer import  CarDetailsSerializer, CarModelSerializer, CountrySerializer, ManufacturerSerializer,\
    SectionSerializer,ProductSerializer


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
    permission_classes = [IsAuthenticated, IsSellerUser]
    queryset = Sections.objects.all()
    serializer_class = SectionSerializer

class SectionListCreateViewworkshop(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsWorkShopUser]
    queryset = Sections.objects.all()

    def get_queryset(self):
        return Sections.objects.filter(user=self.request.user)
    serializer_class = SectionSerializer

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,IsWorkShopUser]
    queryset = Sections.objects.all()
    def get_queryset(self):
        return Sections.objects.filter(user=self.request.user)

    serializer_class = SectionSerializer

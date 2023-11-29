
# Create your views here.
from requests import Response
from rest_framework import viewsets, status
from dj_rest_auth.views import LoginView

from rest_framework import status
from rest_framework.authtoken.models import Token

from .Serializer import DriverSerializer, SellerSerializer, WorkshopSerializer, CustomerSerializer, CustomTokenSerializer


from .models import Driver,Seller,Workshop,Customer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer




class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#create class login for this up and reuern tokne and email username
class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        # Call the parent's post method to complete the login process
        response = super().post(request, *args, **kwargs)

        # Check if the login was successful
        if response.status_code == status.HTTP_200_OK:
            # Get the user associated with the request
            user = self.user
            # Get or create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            # Add user information and token to the response data
            response.data['user_id'] = user.id
            response.data['username'] = user.username
            response.data['email'] = user.email
         

            response.accepted_renderer = response.accepted_media_type = None
            response.renderer_context = {}

        return response
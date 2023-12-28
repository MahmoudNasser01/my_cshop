from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from .cart import Basket
from cardb.views import IsSellerUser

from cardb.models import Products

from cardb.Serializer import AddToBasketSerializer, BasketItemSerializer, BasketSummarySerializer



class BaseBasketView:
    queryset = []
    def get_basket_summary_response(self, basket):
        # Get the updated basket summary
        basket_summary = basket.get_basket_summary()

        # Serialize the basket summary
        serializer = BasketSummarySerializer(data=basket_summary)
        serializer.is_valid(raise_exception=True)

        # Return the serialized data in the response
        return Response(serializer.data)

class AddToBasketView(generics.ListCreateAPIView, BaseBasketView):
    queryset = []
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]
    serializer_class = AddToBasketSerializer

    def get(self, request, *args, **kwargs):
        basket = Basket(request)


        basket_summary = basket.get_basket_summary()

        return Response(basket_summary, status=status.HTTP_201_CREATED)



    # Retrieve the basket summary


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Add the product to the shopping basket
        basket = Basket(request)
        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']
        basket.add_product(product_id, quantity)


        basket_summary = basket.get_basket_summary()



        return Response(basket_summary, status=status.HTTP_201_CREATED)

class UpdateBasketView(APIView, BaseBasketView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]
    serializer_class = AddToBasketSerializer
    def delete(self, request, product_id):
        basket = Basket(request)
        basket.remove_product(product_id)
        return Response(basket.get_basket_summary(), status=status.HTTP_201_CREATED)

class UpdateBasketView_quy(APIView, BaseBasketView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]
    serializer_class = AddToBasketSerializer
    def delete(self, request, product_id):
        basket = Basket(request)
        basket.remove_product_quantity(product_id)
        return Response(basket.get_basket_summary(), status=status.HTTP_201_CREATED)





class ClearBasketAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsSellerUser]
    serializer_class = AddToBasketSerializer
    def delete(self, request, *args, **kwargs):
        basket = Basket(request)
        basket.clear_basket()
        return Response(basket.get_basket_summary(),status=status.HTTP_204_NO_CONTENT)
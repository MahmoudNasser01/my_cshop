from django.urls import path, include

from .views import AddToBasketView,UpdateBasketView_quy,\
    ClearBasketAPIView, UpdateBasketView

urlpatterns = [
path('api/',AddToBasketView.as_view() , name='cart-view'),

    path('api/<int:product_id>/', UpdateBasketView.as_view(), name='update-basket'),
path('api/tity/<int:product_id>/', UpdateBasketView_quy.as_view(), name='update-basket'),
path('api/clear/', ClearBasketAPIView.as_view(), name='clear-basket'),

]


from django.urls import path, include



from .views import (
    CountryListCreateView, ManufacturerListCreateView, CarModelListCreateView,
    CarDetailsListCreateView, CarDetailsDetailView, SectionListCreateView, SectionListCreateViewworkshop,
    SectionDetailView, OrderDetailView, OrderListCreateView, DeliveryListCreateView,
    ProductListCreateView, ProductDetailView,
    ProductListCreateViewwork,
)

urlpatterns = [
    path('countries/', CountryListCreateView.as_view({'get': 'list'}), name='country-list'),
    path('manufacturers/', ManufacturerListCreateView.as_view({'get': 'list'}), name='manufacturer-list'),
    path('car-model/', CarModelListCreateView.as_view({'get': 'list'}), name='car-model-list'),
    path('car-details/', CarDetailsListCreateView.as_view(), name='car-details-list-create'),
    path('car-details/<int:pk>/', CarDetailsDetailView.as_view(), name='car-details-detail'),
   #this is for work shop and seller product
    path('sections/', SectionListCreateView.as_view({'get': 'list'}), name='sections-list'),
    path('sectionsworkshop/', SectionListCreateViewworkshop.as_view(), name='sectionswork-list'),
    path('sectionsworkshop/<int:pk>/', SectionDetailView.as_view(), name='sections-detail'),
    path('products/', ProductListCreateView.as_view(), name='products-list'),
    path('productsworkshop/', ProductListCreateViewwork.as_view(), name='productswork-list'),
    path('productsworkshop/<int:pk>/', ProductDetailView.as_view(), name='products-detail'),
    # cart
    path('order/', OrderListCreateView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('delivery/', DeliveryListCreateView.as_view(), name='delivery-list'),




]



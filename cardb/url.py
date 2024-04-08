from django.urls import path, include



from .views import (
    CountryListCreateView, ManufacturerListCreateView, CarModelListCreateView,
    CarDetailsListCreateView, CarDetailsDetailView, SectionListCreateView, SectionListCreateViewworkshop,
    SectionDetailView, OrderDetailView, OrderListCreateView, DeliveryListCreateView,
    ProductListCreateView, ProductDetailView,
    ProductListCreateViewwork, DeliveryList_workshop, DeliveryDetailView, Delivery_driver, Delivery_driverlist,
AddDeliveryView,AddDeliveryView_edit_status,AddDeliveryView_edit_rejected,AddDeliveryView_edit_completed,AddDeliveryView_edit_pending,
    Delivery_driverview
)
# iuse  try except
try:
    urlpatterns = [
        path('countries/', CountryListCreateView.as_view({'get': 'list'}), name='country-list'),
        path('manufacturers/', ManufacturerListCreateView.as_view({'get': 'list'}), name='manufacturer-list'),
        path('car-model/', CarModelListCreateView.as_view({'get': 'list'}), name='car-model-list'),
        path('car-details/', CarDetailsListCreateView.as_view(), name='car-details-list-create'),
        path('car-details/<int:pk>/', CarDetailsDetailView.as_view(), name='car-details-detail'),
        # this is for work shop and seller product
        path('sections/', SectionListCreateView.as_view({'get': 'list'}), name='sections-list'),
        path('sectionsworkshop/', SectionListCreateViewworkshop.as_view(), name='sectionswork-list'),
        path('sectionsworkshop/<int:pk>/', SectionDetailView.as_view(), name='sections-detail'),
        path('products/', ProductListCreateView.as_view(), name='products-list'),
        path('productsworkshop/', ProductListCreateViewwork.as_view(), name='productswork-list'),
        path('productsworkshop/<int:pk>/', ProductDetailView.as_view(), name='products-detail'),
        path('deliverydriver/', Delivery_driverview.as_view(), name='deliverydriver-list'),
        path('deliverydriver/<int:pk>/', Delivery_driverlist.as_view(), name='deliverydriver-detail'),
        path('deliveryadd/', AddDeliveryView.as_view(), name='add-delivery'),
        path('delivery/<int:pk>/', AddDeliveryView_edit_status.as_view(), name='edit-delivery'),
        path('delivery/rejected/', AddDeliveryView_edit_rejected.as_view(), name='edit-delivery-rejected'),
        path('delivery/completed/', AddDeliveryView_edit_completed.as_view(), name='edit-delivery-completed'),
        path('delivery/pending/', AddDeliveryView_edit_pending.as_view(), name='edit-delivery-pending'),

        # cart
        path('order/', OrderListCreateView.as_view(), name='order-list'),
        path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
        path('delivery/', DeliveryListCreateView.as_view(), name='delivery-list'),
        path('deliveryworkshop/', DeliveryList_workshop.as_view(), name='deliverywork-list'),
        path('deliveryworkshop/<int:pk>/', DeliveryDetailView.as_view(), name='delivery-detail'),

    ]
except:
    pass





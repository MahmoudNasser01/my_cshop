from django.urls import path, include



from .views import (
    CountryListCreateView, ManufacturerListCreateView, CarModelListCreateView,
    CarDetailsListCreateView, CarDetailsDetailView,SectionListCreateView,SectionListCreateViewworkshop,SectionDetailView
)

urlpatterns = [
    path('countries/', CountryListCreateView.as_view({'get': 'list'}), name='country-list'),
    path('manufacturers/', ManufacturerListCreateView.as_view({'get': 'list'}), name='manufacturer-list'),
    path('car-model/', CarModelListCreateView.as_view({'get': 'list'}), name='car-model-list'),
    path('car-details/', CarDetailsListCreateView.as_view(), name='car-details-list-create'),
    path('car-details/<int:pk>/', CarDetailsDetailView.as_view(), name='car-details-detail'),
    path('sections/', SectionListCreateView.as_view({'get': 'list'}), name='sections-list'),
    path('sectionsworkshop/', SectionListCreateViewworkshop.as_view(), name='sectionswork-list'),
    path('sectionsworkshop/<int:pk>/', SectionDetailView.as_view(), name='sections-detail'),


]
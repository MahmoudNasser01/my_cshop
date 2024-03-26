from allauth.account.views import ConfirmEmailView
from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView

from django.urls import path, include
from rest_framework import routers

from .views import DriverViewSet, SellerViewSet, WorkshopViewSet, CustomerViewSet, CustomLoginView, SellerMoreViewSet, \
    DriverMoreViewSet, WorkshopMoreViewSet



router = routers.DefaultRouter()
router.register(r'drivers', DriverViewSet)
router.register(r'driversmore', DriverMoreViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'sellersmore', SellerMoreViewSet)
router.register(r'workshops', WorkshopViewSet)
router.register(r'workshopsmore', WorkshopMoreViewSet)

router.register(r'customers', CustomerViewSet)




urlpatterns = [

path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    #path('register/', RegisterView.as_view()),

    path('login/',CustomLoginView.as_view(), name='custom-login'),

    path('logout/', LogoutView.as_view()),

    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),
    path('', include(router.urls)),
]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path

from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

from utils.send_email import EmailThread


def test_email(request):
    EmailThread(
        subject="Monthly Subscriptions Report",
        message="Monthly Subscriptions Report attached",
        html_message="Monthly Subscriptions Report attached",
        to_email="vego2000im@gmail.com",
    ).start()

    return HttpResponse('send')


urlpatterns = [
    path('test_email', test_email),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('cshop/', include('cardb.url')),
    path('cart/', include('cart.urls')),

    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

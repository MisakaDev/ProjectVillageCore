from django.urls import path
from rest_auth.views import LogoutView

from .views import Login
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/', csrf_exempt(Login.as_view())),
    path('logout/', csrf_exempt(LogoutView.as_view())),
]

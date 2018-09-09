from django.urls import path
from rest_auth.views import LogoutView

from .views import Login

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', LogoutView.as_view()),
]

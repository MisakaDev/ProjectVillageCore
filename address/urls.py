from django.urls import path

from .views import CityList

urlpatterns = [
    path('city/', CityList.as_view()),
]

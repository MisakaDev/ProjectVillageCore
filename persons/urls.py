from django.urls import path

from .views import IndividualPersonList, IndividualPersonDetail

urlpatterns = [
    path('individual/', IndividualPersonList.as_view()),
    path('individual/<int:pk>/', IndividualPersonDetail.as_view()),
]

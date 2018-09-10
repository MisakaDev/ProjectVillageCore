from django.urls import path

from .views import IndividualPersonList, IndividualPersonDetail, LegalPersonList, LegalPersonDetail

urlpatterns = [
    # Individual person
    path('individual/', IndividualPersonList.as_view()),
    path('individual/<int:pk>/', IndividualPersonDetail.as_view()),
    # Legal person
    path('legal/', LegalPersonList.as_view()),
    path('legal/<int:pk>/', LegalPersonDetail.as_view()),
]

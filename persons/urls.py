from django.urls import path

from .views import IndividualPersonList, IndividualPersonDetail, LegalPersonList, LegalPersonDetail, \
    IndividualPersonListSearch, LegalPersonListSearch

urlpatterns = [
    # Individual person
    path('individual/', IndividualPersonList.as_view()),
    path('individual_search/', IndividualPersonListSearch.as_view()),
    path('individual/<int:pk>/', IndividualPersonDetail.as_view()),
    # Legal person
    path('legal/', LegalPersonList.as_view()),
    path('legal_search/', LegalPersonListSearch.as_view()),
    path('legal/<int:pk>/', LegalPersonDetail.as_view()),
]

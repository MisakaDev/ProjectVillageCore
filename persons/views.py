from rest_framework import generics, filters

from .filters import IndividualPersonFilter, LegalPersonFilter
from .models import IndividualPerson, LegalPerson
from .serializers import IndividualPersonSerializer, LegalPersonSerializer


class IndividualPersonList(generics.ListCreateAPIView):
    queryset = IndividualPerson.objects.all()
    serializer_class = IndividualPersonSerializer
    filterset_class = IndividualPersonFilter


class IndividualPersonListSearch(generics.ListCreateAPIView):
    queryset = IndividualPerson.objects.all()
    serializer_class = IndividualPersonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'middle_name', 'inn')


class IndividualPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndividualPerson.objects.all()
    serializer_class = IndividualPersonSerializer


class LegalPersonList(generics.ListCreateAPIView):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer
    filterset_class = LegalPersonFilter


class LegalPersonListSearch(generics.ListCreateAPIView):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'edrpou')


class LegalPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer

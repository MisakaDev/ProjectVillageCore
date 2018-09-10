from rest_framework import generics

from .filters import IndividualPersonFilter, LegalPersonFilter
from .models import IndividualPerson, LegalPerson
from .serializers import IndividualPersonSerializer, LegalPersonSerializer


class IndividualPersonList(generics.ListCreateAPIView):
    queryset = IndividualPerson.objects.all()
    serializer_class = IndividualPersonSerializer
    filterset_class = IndividualPersonFilter


class IndividualPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndividualPerson.objects.all()
    serializer_class = IndividualPersonSerializer


class LegalPersonList(generics.ListCreateAPIView):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer
    filterset_class = LegalPersonFilter


class LegalPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer

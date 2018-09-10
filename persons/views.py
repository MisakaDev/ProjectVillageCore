from rest_framework import generics

from .filters import IndividualPersonFilter
from .models import IndividualPerson
from .serializers import IndividualPersonSerializer


class IndividualPersonList(generics.ListCreateAPIView):
    queryset = IndividualPerson.objects.all()
    serializer_class = IndividualPersonSerializer
    filterset_class = IndividualPersonFilter


class IndividualPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndividualPerson.objects.all()
    serializer_class = IndividualPersonSerializer

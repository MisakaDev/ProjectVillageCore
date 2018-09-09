from rest_framework import generics

from .filters import CityFilter
from .models import City
from .serializers import CitySerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter

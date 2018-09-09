from rest_framework import generics

from .models import City
from .serializers import CitySerializer


class CityList(generics.ListAPIView):
    """
    Query params:
        - name: filtering by city name
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get('name')
        if name:
            return queryset.filter(name__contains=name).all()
        return queryset.all()

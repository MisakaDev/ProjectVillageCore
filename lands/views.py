from rest_framework import generics, filters

from .filters import LandPlotFilter, LandOwnFilter, LandRentFilter
from .models import LandPurpose, LandUnit, LandPlot, LandOwn, LandRent
from .serializers import LandPurposeSerializer, LandUnitSerializer, LandPlotSerializer, LandOwnSerializer
from .serializers import LandRentSerializer


class LandPurposeList(generics.ListAPIView):
    queryset = LandPurpose.objects.all()
    serializer_class = LandPurposeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('code', 'name')


class LandUnitList(generics.ListAPIView):
    queryset = LandUnit.objects.all()
    serializer_class = LandUnitSerializer


class LandPlotList(generics.ListCreateAPIView):
    queryset = LandPlot.objects.all()
    serializer_class = LandPlotSerializer
    filterset_class = LandPlotFilter


class LandPlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LandPlot.objects.all()
    serializer_class = LandPlotSerializer


class LandOwnList(generics.ListCreateAPIView):
    queryset = LandOwn.objects.all()
    serializer_class = LandOwnSerializer
    filterset_class = LandOwnFilter


class LandRentList(generics.ListCreateAPIView):
    queryset = LandRent.objects.all()
    serializer_class = LandRentSerializer
    filterset_class = LandRentFilter

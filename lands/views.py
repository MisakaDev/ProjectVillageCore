from rest_framework import generics, filters

from .filters import LandPlotFilter
from .models import LandPurpose, LandUnit, LandPlot
from .serializers import LandPurposeSerializer, LandUnitSerializer, LandPlotSerializer


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

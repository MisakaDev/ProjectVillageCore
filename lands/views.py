from django.db.models import Sum
from rest_framework import generics, filters, views, response

from .filters import LandPlotFilter, LandOwnFilter, LandRentFilter
from .models import LandPurpose, LandUnit, LandPlot, LandOwn, LandRent, LandZone
from .serializers import LandPurposeSerializer, LandUnitSerializer, LandPlotSerializer, LandOwnSerializer, \
    LandZoneSerializer
from .serializers import LandRentSerializer


class LandPurposeList(generics.ListAPIView):
    queryset = LandPurpose.objects.all()
    serializer_class = LandPurposeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('code', 'name')


class LandUnitList(generics.ListAPIView):
    queryset = LandUnit.objects.all()
    serializer_class = LandUnitSerializer


class LandZoneList(generics.ListAPIView):
    queryset = LandZone.objects.all()
    serializer_class = LandZoneSerializer


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


class LandStatistic(views.APIView):
    queryset = LandPlot.objects.all()

    def get(self, request):
        if request.GET.get('type') == 'purpose':
            result = [
                         [""],
                         ["Проща, га"],
                     ],
            data = {purpose.name: purpose.land_plots.aggregate(Sum('area'))['area__sum'] for purpose in
                    LandPurpose.objects.all()}
            for (name, value) in data.items():
                result[0][0].append(name)
                result[0][1].append(value if value else 0)
            return response.Response(result)

        if request.GET.get('type') == 'zone':
            result = [
                         [""],
                         ["Проща, га"],
                     ],
            data = {str(zone): zone.quarters.aggregate(Sum('land_plots__area'))['land_plots__area__sum'] for zone in
                    LandZone.objects.all()}
            for (name, value) in data.items():
                result[0][0].append(name)
                result[0][1].append(value if value else 0)
            return response.Response(result)
        return response.Response({})

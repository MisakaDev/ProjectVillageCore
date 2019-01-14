from django.db.models import Sum
from rest_framework import generics, filters, views, response

from .filters import LandPlotFilter, LandOwnFilter, LandRentFilter
from .models import LandPurpose, LandUnit, LandPlot, LandOwn, LandRent, LandZone
from .serializers import LandPurposeSerializer, LandUnitSerializer, LandPlotSerializer, LandOwnSerializer, \
    LandZoneSerializer
from .serializers import LandRentSerializer

from django.views.generic import ListView
from django.db import connection
import csv
from django.shortcuts import HttpResponse


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


class LandExport(ListView):
    model = LandPlot

    def render_to_response(self, context, **response_kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_export.csv"'

        writer = csv.writer(response)

        # Всі земельні ділянки для який визначено одного власника
        # query = self.get_queryset().annotate(num_owners=Count('owners__person')).filter(num_owners__gt=1)
        with connection.cursor() as cursor:
            cursor.execute("""select 

persons_individualperson.last_name,
persons_individualperson.first_name,
persons_individualperson.middle_name,
persons_individualperson.inn,
persons_person.address,
address_city.name,
address_district.name,
address_region.name,
persons_person.additional_info,

lands_landunit.code || ':' ||
LPAD(to_char(lands_landzone.code, 'FM00'), 2, '0')  || ':' ||
COALESCE(LPAD(to_char(lands_landquarter.code, 'FM000'), 3, '0'), '000') || ':' ||
COALESCE(LPAD(to_char(lands_landplot.code, 'FM0000'), 4, '0'), '0000'),


replace(lands_landplot.area::text, '.', ','),

lands_landpurpose.code,
lands_landpurpose.name,

lands_landplot.address,
lands_landzone.name,
lands_landunit.name,
lands_landplot.additional_info

from lands_landplot 
join lands_landown on lands_landplot.id=lands_landown.land_plot_id

join lands_landpurpose on lands_landplot.purpose_id=lands_landpurpose.id

join lands_landquarter on lands_landplot.quarter_id=lands_landquarter.id
join lands_landzone on lands_landquarter.zone_id=lands_landzone.id
join lands_landunit on lands_landzone.unit_id=lands_landunit.id

join persons_person on lands_landown.person_id=persons_person.id
join persons_individualperson on persons_person.id=persons_individualperson.person_ptr_id

join address_city on persons_person.city_id=address_city.id
join address_district on address_city.district_id=address_district.id
join address_region on address_district.region_id=address_region.id

order by persons_individualperson.last_name, persons_individualperson.first_name, persons_individualperson.middle_name""")
            writer.writerow(['Прізвище',
                             'Ім\'я',
                             'По батькові',
                             'ІНН',
                             'Адрес, Вулиця',
                             'Адрес, Населений пункт',
                             'Адрес, Район',
                             'Адрес, Область',
                             'Коментар про особу',
                             'Кадастровий номер',
                             'Площа',
                             'Призначення, Код',
                             'Призначення, Назва',
                             'Адрес, Вулиця',
                             'С.р',
                             'Село',
                             'Коментар про ділянку',
                             ])
            for row in cursor.fetchall():
                writer.writerow(row)

        return response

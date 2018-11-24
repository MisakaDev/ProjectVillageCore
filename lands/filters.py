from django_filters.rest_framework import FilterSet, NumberFilter, ModelChoiceFilter

from persons.models import Person
from .models import LandPlot, LandPurpose, LandOwn, LandRent, LandZone


class LandPlotFilter(FilterSet):
    area = NumberFilter(field_name='area')
    purpose = ModelChoiceFilter(queryset=LandPurpose.objects.all())
    quarter__zone = ModelChoiceFilter(queryset=LandZone.objects.all())
    code = NumberFilter()
    quarter__code = NumberFilter()
    quarter__zone__code = NumberFilter()
    quarter__zone__unit__code = NumberFilter()

    class Meta:
        model = LandPlot
        fields = ('area', 'purpose', 'quarter__zone', 'code', 'quarter__code', 'quarter__zone__code',
                  'quarter__zone__unit__code')


class LandOwnFilter(FilterSet):
    person = ModelChoiceFilter(queryset=Person.objects.all())
    land_plot = ModelChoiceFilter(queryset=LandPlot.objects.all())

    class Meta:
        model = LandOwn
        fields = ('person', 'land_plot')


class LandRentFilter(FilterSet):
    person = ModelChoiceFilter(queryset=Person.objects.all())
    land_plot = ModelChoiceFilter(queryset=LandPlot.objects.all())

    class Meta:
        model = LandRent
        fields = ('person',)

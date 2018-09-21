from django_filters.rest_framework import FilterSet, NumberFilter, ModelChoiceFilter

from persons.models import Person
from .models import LandPlot, LandPurpose, LandOwn, LandRent


class LandPlotFilter(FilterSet):
    area = NumberFilter(field_name='area')
    purpose = ModelChoiceFilter(queryset=LandPurpose.objects.all())

    class Meta:
        model = LandPlot
        fields = ('area', 'purpose')


class LandOwnFilter(FilterSet):
    person = ModelChoiceFilter(queryset=Person.objects.all())

    class Meta:
        model = LandOwn
        fields = ('person',)


class LandRentFilter(FilterSet):
    person = ModelChoiceFilter(queryset=Person.objects.all())

    class Meta:
        model = LandRent
        fields = ('person',)

from django_filters.rest_framework import FilterSet, NumberFilter, ModelChoiceFilter

from .models import LandPlot, LandPurpose


class LandPlotFilter(FilterSet):
    area = NumberFilter(field_name='area')
    purpose = ModelChoiceFilter(queryset=LandPurpose.objects.all())

    class Meta:
        model = LandPlot
        fields = ('area', 'purpose')

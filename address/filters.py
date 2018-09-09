from django_filters.rest_framework import FilterSet, CharFilter

from .models import City


class CityFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = City
        fields = ['name', ]

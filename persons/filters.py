from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter, ModelChoiceFilter

from address.models import City
from .models import IndividualPerson


class IndividualPersonFilter(FilterSet):
    last_name = CharFilter(field_name="last_name", lookup_expr='icontains')
    first_name = CharFilter(field_name="first_name", lookup_expr='icontains')
    middle_name = CharFilter(field_name="middle_name", lookup_expr='icontains')
    inn = NumberFilter(field_name="inn", lookup_expr='icontains')
    city = ModelChoiceFilter(field_name='city', queryset=City.objects.all())
    address = CharFilter(field_name="address", lookup_expr='icontains')
    additional_info = CharFilter(field_name="additional_info", lookup_expr='icontains')

    class Meta:
        model = IndividualPerson
        fields = ['last_name', 'first_name', 'middle_name', 'inn', 'city', 'address', 'additional_info']

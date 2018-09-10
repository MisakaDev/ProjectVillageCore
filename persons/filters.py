from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter, ModelChoiceFilter

from address.models import City
from .models import Person, IndividualPerson, LegalPerson


class PersonFilter(FilterSet):
    city = ModelChoiceFilter(field_name='city', queryset=City.objects.all())
    address = CharFilter(field_name="address", lookup_expr='icontains')
    additional_info = CharFilter(field_name="additional_info", lookup_expr='icontains')

    class Meta:
        model = Person
        fields = ('city', 'address', 'additional_info')


class IndividualPersonFilter(PersonFilter):
    last_name = CharFilter(field_name="last_name", lookup_expr='icontains')
    first_name = CharFilter(field_name="first_name", lookup_expr='icontains')
    middle_name = CharFilter(field_name="middle_name", lookup_expr='icontains')
    inn = NumberFilter(field_name="inn", lookup_expr='icontains')

    class Meta(PersonFilter.Meta):
        model = IndividualPerson
        fields = ('last_name', 'first_name', 'middle_name', 'inn') + PersonFilter.Meta.fields


class LegalPersonFilter(PersonFilter):
    name = CharFilter(field_name="name", lookup_expr='icontains')
    edrpou = NumberFilter(field_name='edrpou', lookup_expr='icontains')

    class Meta(PersonFilter.Meta):
        model = LegalPerson
        fields = ('name', 'edrpou') + PersonFilter.Meta.fields

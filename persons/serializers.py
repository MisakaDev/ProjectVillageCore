from rest_framework import serializers

from address.models import City
from address.serializers import CitySerializer
from profiles.serializers import ProfileSerializer
from .models import Person, IndividualPerson, LegalPerson


class PersonSerializer(serializers.ModelSerializer):
    created_by = ProfileSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    edited_by = ProfileSerializer(read_only=True)
    edited_at = serializers.DateTimeField(read_only=True)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), write_only=True)
    city_name = CitySerializer(source='city', read_only=True)
    additional_info = serializers.CharField(required=False, default='', allow_blank=True)

    def create(self, validated_data):
        current_user = self.context['request'].user.profile
        validated_data['created_by'] = current_user
        validated_data['edited_by'] = current_user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        current_user = self.context['request'].user.profile
        validated_data['edited_by'] = current_user
        return super().update(instance, validated_data)

    class Meta:
        model = Person
        fields = ('id', 'city', 'city_name', 'address', 'additional_info', 'created_by', 'created_at',
                  'edited_by', 'edited_at')


class IndividualPersonSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model = IndividualPerson
        fields = ('last_name', 'first_name', 'middle_name', 'inn') + PersonSerializer.Meta.fields


class LegalPersonSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model = LegalPerson
        fields = ('name', 'edrpou') + PersonSerializer.Meta.fields

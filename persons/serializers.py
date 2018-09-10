from rest_framework import serializers

from address.models import City
from address.serializers import CitySerializer
from profiles.serializers import ProfileSerializer
from .models import IndividualPerson


class IndividualPersonSerializer(serializers.ModelSerializer):
    additional_info = serializers.CharField(required=False, default='')
    created_by = ProfileSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    edited_by = ProfileSerializer(read_only=True)
    edited_at = serializers.DateTimeField(read_only=True)

    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), write_only=True)
    city_name = CitySerializer(source='city', read_only=True)

    class Meta:
        model = IndividualPerson
        fields = (
            'id', 'last_name', 'first_name', 'middle_name', 'inn', 'city', 'city_name', 'address', 'additional_info',
            'created_by', 'created_at', 'edited_by', 'edited_at')

    def create(self, validated_data):
        current_user = self.context['request'].user.profile
        validated_data['created_by'] = current_user
        validated_data['edited_by'] = current_user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        current_user = self.context['request'].user.profile
        validated_data['edited_by'] = current_user
        return super().update(instance, validated_data)

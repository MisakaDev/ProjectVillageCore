from rest_framework import serializers

from .models import City


class CitySerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district.name')
    region_name = serializers.CharField(source='district.region.name')

    class Meta:
        model = City
        fields = ('id', 'name', 'district_name', 'region_name')

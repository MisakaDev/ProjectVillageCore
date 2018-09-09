from rest_framework import serializers

from .models import City


class CitySerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district.name')
    region_name = serializers.CharField(source='district.region.name')
    city_name = serializers.CharField(source='name')

    class Meta:
        model = City
        fields = ('id', 'city_name', 'district_name', 'region_name')

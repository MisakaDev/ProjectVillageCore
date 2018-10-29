from rest_framework import serializers

from profiles.serializers import ProfileSerializer
from .models import LandPurpose, LandZone, LandUnit, LandPlot, LandQuarter, LandOwn, LandRent


class LandPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandPurpose
        fields = ('id', 'code', 'name')


class LandZoneSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.name')
    unit_code = serializers.CharField(source='unit.code')

    class Meta:
        model = LandZone
        fields = ('id', 'code', 'name', 'unit_name', 'unit_code')


class LandUnitSerializer(serializers.ModelSerializer):
    zones = LandZoneSerializer(many=True)

    class Meta:
        model = LandUnit
        fields = ('id', 'code', 'name', 'zones')


class LandQuarterSerializer(serializers.ModelSerializer):
    zone_id = serializers.IntegerField(source='zone.id')
    zone_code = serializers.IntegerField(source='zone.code')
    zone_name = serializers.CharField(source='zone.name')
    unit_id = serializers.IntegerField(source='zone.unit.id')
    unit_code = serializers.IntegerField(source='zone.unit.code')
    unit_name = serializers.CharField(source='zone.unit.name')

    class Meta:
        model = LandQuarter
        fields = ('id', 'code', 'zone_id', 'zone_code', 'zone_name', 'unit_id', 'unit_code', 'unit_name')


class LandPlotSerializer(serializers.ModelSerializer):
    quarter_info = LandQuarterSerializer(source='quarter', read_only=True)
    zone = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LandZone.objects.all())
    quarter = serializers.IntegerField(write_only=True, allow_null=True)
    created_by = ProfileSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    edited_by = ProfileSerializer(read_only=True)
    edited_at = serializers.DateTimeField(read_only=True)
    additional_info = serializers.CharField(allow_blank=True)
    purpose_info = LandPurposeSerializer(source='purpose', read_only=True)

    class Meta:
        model = LandPlot
        fields = ('id', 'zone', 'quarter', 'quarter_info', 'code', 'area', 'purpose', 'address', 'additional_info',
                  'created_by', 'created_at', 'edited_by', 'edited_at', 'purpose_info')

    def create(self, validated_data):
        current_user = self.context['request'].user.profile
        validated_data['created_by'] = current_user
        validated_data['edited_by'] = current_user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        current_user = self.context['request'].user.profile
        validated_data['edited_by'] = current_user
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        quarter, _ = LandQuarter.objects.get_or_create(code=self.validated_data.pop('quarter', None),
                                                       zone=self.validated_data.pop('zone'))
        self.validated_data['quarter'] = quarter
        return super().save(**kwargs)


class LandOwnSerializer(serializers.ModelSerializer):
    land_plot_info = LandPlotSerializer(source='land_plot', read_only=True)
    land_plot = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LandPlot.objects.all())

    class Meta:
        model = LandOwn
        fields = ('person', 'land_plot', 'land_plot_info')


class LandRentSerializer(serializers.ModelSerializer):
    land_plot_info = LandPlotSerializer(source='land_plot', read_only=True)
    land_plot = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LandPlot.objects.all())

    class Meta:
        model = LandRent
        fields = ('person', 'land_plot', 'land_plot_info')

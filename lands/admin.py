from django.contrib import admin

from .models import LandPurpose, LandUnit, LandZone, LandQuarter


class SearchLandPurpose(admin.ModelAdmin):
    search_fields = ('code', 'name')


admin.site.register(LandPurpose, SearchLandPurpose)
admin.site.register(LandUnit)
admin.site.register(LandZone)
admin.site.register(LandQuarter)

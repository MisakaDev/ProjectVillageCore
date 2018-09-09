from django.contrib import admin

from .models import Region, District, City


class SearchAddress(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Region, SearchAddress)
admin.site.register(District, SearchAddress)
admin.site.register(City, SearchAddress)

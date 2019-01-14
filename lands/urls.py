from django.urls import path

from .views import LandPurposeList, LandUnitList, LandPlotList, LandPlotDetail, LandOwnList, LandRentList, LandZoneList, \
    LandStatistic, LandExport

urlpatterns = [
    path('purpose/', LandPurposeList.as_view()),
    path('unit/', LandUnitList.as_view()),
    path('zone/', LandZoneList.as_view()),
    path('', LandPlotList.as_view()),
    path('<int:pk>/', LandPlotDetail.as_view()),
    path('own/', LandOwnList.as_view()),
    path('rent/', LandRentList.as_view()),
    path('stats/', LandStatistic.as_view()),
    path('export/', LandExport.as_view()),
]

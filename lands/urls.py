from django.urls import path

from .views import LandPurposeList, LandUnitList, LandPlotList, LandPlotDetail

urlpatterns = [
    path('purpose/', LandPurposeList.as_view()),
    path('unit/', LandUnitList.as_view()),
    path('', LandPlotList.as_view()),
    path('<int:pk>/', LandPlotDetail.as_view()),
]
from django.urls import path

from profiles.views import ProfileView

urlpatterns = [
    path('', ProfileView.List.as_view()),
    path('<int:pk>', ProfileView.Detail.as_view()),
]

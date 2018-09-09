from rest_framework import generics

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileView:
    class List(generics.ListAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer

    class Detail(generics.RetrieveUpdateAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer

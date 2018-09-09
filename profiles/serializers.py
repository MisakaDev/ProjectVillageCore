from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    post = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'post')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})

        instance = super().update(instance, validated_data)

        if user_data:
            instance.user.first_name = user_data.get('first_name', '')
            instance.user.last_name = user_data.get('last_name', '')
            instance.user.save()
        return instance

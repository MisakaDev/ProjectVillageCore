from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.CharField("Посада", max_length=255)

    class Meta:
        ordering = ('user__id',)

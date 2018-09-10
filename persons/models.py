from django.db import models

from address.models import City
from profiles.models import Profile


class Person(models.Model):
    city = models.ForeignKey(City, models.PROTECT)
    address = models.CharField(max_length=255)
    created_by = models.ForeignKey(Profile, models.PROTECT, related_name='person_created')
    created_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(Profile, models.PROTECT, related_name='person_edited')
    edited_at = models.DateTimeField(auto_now=True)
    additional_info = models.TextField()


class IndividualPerson(Person):
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    inn = models.BigIntegerField(unique=True)

    class Meta:
        ordering = ['last_name', 'first_name', 'middle_name', 'inn']


class LegalPerson(Person):
    name = models.CharField(max_length=64)
    edrpou = models.IntegerField(unique=True)

    class Meta:
        ordering = ['name', 'edrpou']

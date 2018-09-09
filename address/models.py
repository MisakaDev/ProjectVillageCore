from django.db import models


class Region(models.Model):
    name = models.CharField("Назва", max_length=64, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class District(models.Model):
    name = models.CharField("Назва", max_length=64)
    region = models.ForeignKey(Region, models.CASCADE, 'districts')

    class Meta:
        ordering = ('name',)
        unique_together = (('name', 'region'),)

    def __str__(self):
        return "{}, {}".format(self.name, self.region)


class City(models.Model):
    name = models.CharField("Назва", max_length=64)
    district = models.ForeignKey(District, models.CASCADE, 'cities')

    class Meta:
        ordering = ('name',)
        unique_together = (('name', 'district'),)

    def __str__(self):
        return "{}, {}".format(self.name, self.district)

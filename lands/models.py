from django.db import models

from profiles.models import Profile


class LandPurpose(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=1024)

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return "{} {}".format(self.code, self.name)


class LandUnit(models.Model):
    code = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return "{:010} {}".format(self.code, self.name)


class LandZone(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=64)
    unit = models.ForeignKey(LandUnit, models.PROTECT, 'zones')

    class Meta:
        ordering = ('code',)
        unique_together = (('unit', 'code'),)

    def __str__(self):
        return "{} - {:02} {}".format(self.unit, self.code, self.name)


class LandQuarter(models.Model):
    code = models.IntegerField(null=True, blank=True)
    zone = models.ForeignKey(LandZone, models.PROTECT, 'quarters')

    class Meta:
        ordering = ('code',)
        unique_together = (('zone', 'code'),)

    def __str__(self):
        if self.code:
            return "{} - {:03}".format(self.zone, self.code)
        return "{} - Без кадастрового номера".format(self.zone)


class LandPlot(models.Model):
    quarter = models.ForeignKey(LandQuarter, models.PROTECT, 'land_plots')
    code = models.IntegerField(null=True, blank=True)
    purpose = models.ForeignKey(LandPurpose, models.PROTECT, 'land_plots')
    area = models.FloatField()
    address = models.CharField(max_length=64, blank=True, null=True)
    additional_info = models.TextField()
    created_by = models.ForeignKey(Profile, models.PROTECT, related_name='lands_created')
    created_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(Profile, models.PROTECT, related_name='lands_edited')
    edited_at = models.DateTimeField(auto_now=True)


""" A django model generated with django-csvimport csvinspect
    which used OKN messytables to guess data types - may need some manual tweaks!
"""
from django.db import models


class DisasterIndex(models.Model):
    ''' Autogenerated model file csvimportincidentreport Fri Aug 21 13:59:03 2020 '''

    id = models.IntegerField(primary_key=True, blank=False, null=False, default=0)
    district = models.CharField(max_length=64, blank=True,  default="")
    vdc = models.CharField(max_length=64, blank=True, null=True, default="")
    wardno = models.CharField(max_length=64, blank=True, null=True, default="")
    incidentplace = models.CharField(max_length=64, blank=True, default="")
    incidentdate = models.DateTimeField(blank=True, null=True)
    incidenttype = models.CharField(max_length=64, blank=True, null=True, default="")
    deathmale = models.IntegerField(blank=True, null=True)
    deathfemale = models.IntegerField(blank=True, null=True)
    deathunknown = models.IntegerField(blank=True, null=True)
    totaldeath = models.IntegerField(blank=True, null=True)
    missingpeople = models.IntegerField(blank=True, null=True)
    affectedfamily = models.IntegerField(blank=True, null=True)
    estimatedloss = models.IntegerField(blank=True, null=True)
    injured = models.IntegerField(blank=True, null=True)
    govthousesfullydamaged = models.IntegerField(blank=True, null=True)
    govthousespartiallydamaged = models.IntegerField(blank=True, null=True)
    privatehousesfullydamaged = models.IntegerField(blank=True, null=True)
    privatehousespartiallydamaged = models.IntegerField(blank=True, null=True)
    displacedmale = models.IntegerField(blank=True, null=True)
    displacedfemale = models.IntegerField(blank=True, null=True)
    propertyloss = models.IntegerField(blank=True, null=True)
    noofdisplacedfamily = models.IntegerField(blank=True, null=True)
    cattlesloss = models.IntegerField(blank=True, null=True)
    displacedshed = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=64, blank=True, null=True, default="")
    remarks = models.CharField(max_length=64, blank=True, null=True, default="")

    def __str__(self):
        return self.district+"-"+self.incidenttype

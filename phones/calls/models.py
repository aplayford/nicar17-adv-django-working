from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


@python_2_unicode_compatible
class PhoneCall(models.Model):
    extension = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=14)
    call_date_time = models.DateTimeField()
    duration_in_seconds = models.IntegerField()
    inbound = models.BooleanField()
    employee = models.ForeignKey("Employee", blank=True, null=True)

    def whois(self):
        try:
            return Employee.objects.get(extension = self.extension)
        except:
            return None

    def save(self, *args, **kwargs):
        self.employee = self.whois()
        return super(PhoneCall, self).save(*args, **kwargs)

    def __str__(self):
        if self.inbound:
            return "%s <- %s" % (self.extension, self.phone_number)
        else:
            return "%s -> %s" % (self.extension, self.phone_number)

@python_2_unicode_compatible
class Employee(models.Model):
    name = models.CharField(max_length=45, blank=True)
    business_title = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=50, blank=True)
    extension = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    def get_absolute_url(self): # get this from docs. https://docs.djangoproject.com/en/1.10/ref/models/instances/#get-absolute-url
        return '/employees/%s/' % self.pk

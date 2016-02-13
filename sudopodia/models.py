from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=40)
    TimeStamp = models.DateTimeField("")
    Genre = models.CharField(max_length=20)
    Venue = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Contact = models.CharField(max_length=50)
    Postscript = models.CharField(max_length=50)
    Links = models.CharField(max_length=200)
    Updated = models.BooleanField()

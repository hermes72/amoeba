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
    def __json__(self):
        jsons = '{'
        jsons += '"ID" : "' + str(self.id) + '",'
        jsons += '"Name" : "' + self.Name + '",'
        jsons += '"TimeStamp" : "' + str(self.TimeStamp) + '",'
        jsons += '"Genre" : "' + self.Genre + '",'
        jsons += '"Venue" : "' + self.Venue + '",'
        jsons += '"Description" : "' + self.Description + '",'
        jsons += '"Contact" : "' + self.Contact + '",'
        jsons += '"Postscript" : "' + self.Postscript + '",'
        jsons += '"Links" : "' + self.Links + '",'
        jsons += '"Updated" : "' + str(self.Updated) + '}'
        return jsons

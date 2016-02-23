from __future__ import unicode_literals
import os 
from django.db import models
import hashlib
# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=40)
    TimeStamp = models.CharField(max_length=30)
    Genre = models.CharField(max_length=20)
    Venue = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Contact = models.CharField(max_length=50)
    Postscript = models.CharField(max_length=50)
    Links = models.CharField(max_length=200)
    PostedBy = models.CharField(max_length=100,default="")
    Updated = models.BooleanField(default=False)
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
	jsons += '"PostedBy" : "' + self.PostedBy + '",'
        jsons += '"Updated" : "' + str(self.Updated) + '}'
        return jsons

class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    apikey = models.CharField(max_length=32)
    auth = models.BooleanField(default=False)
    def isauth(self):
        return bool(self.auth)
    def gen(self,name,email):
        self.Name = name
	self.Email = email
	padding = os.urandom(6).encode('hex')
	self.apikey = hashlib.md5(name + padding + email).hexdigest()

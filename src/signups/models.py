from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

# using user profile to extend the default user
class UserProfile(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    image = models.URLField(max_length=500, blank=True, default='https://a3-images.myspacecdn.com/images03/1/240e42b5d9ce48a78983961e7fcb3c39/600x600.jpg')
    user = models.OneToOneField(User)
    def __unicode__(self):
		return self.first_name

class Beacon(models.Model):
	user = models.OneToOneField(User)
	rating = models.IntegerField()

class Hero(models.Model):
	user = models.OneToOneField(User)
	rating = models.IntegerField()

class Quest(models.Model):
	hero = models.OneToOneField(Hero)
	beacon = models.OneToOneField(Beacon)
	name = models.CharField(max_length=120, null=True, blank=True)
	date = models.DateTimeField(null=True)
	location = models.CharField(max_length=120, null=True, blank=True)
	description = models.CharField(max_length=120, null=True, blank=True)


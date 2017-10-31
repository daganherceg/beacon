from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
# NOTE: SignUp is singular
class SignUp(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email

class Quest(models.Model):
	quest_id = models.IntegerField(default=0)
	quest_name = models.CharField(max_length=120, null=True, blank=True)
	quest_contents = models.CharField(max_length=200, null=True, blank=False)
	quest_owner = models.ForeignKey('SignUp', on_delete=models.CASCADE)
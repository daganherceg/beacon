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
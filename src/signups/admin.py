from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "first_name", "last_name"]
	class Meta:
		model = UserProfile

# the name of the entries
admin.site.register(UserProfile, UserProfileAdmin)


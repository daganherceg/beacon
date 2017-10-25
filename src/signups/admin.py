from django.contrib import admin
from .models import SignUp

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "first_name", "last_name", "timestamp"]
	class Meta:
		model = SignUp

# the name of the entries
admin.site.register(SignUp, SignUpAdmin)


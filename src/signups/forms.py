from django import forms
from registration.forms import RegistrationFormUniqueEmail
from .models import Quest

class UserProfileRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    image = forms.URLField()


class CreateQuestForm(forms.ModelForm):
	class Meta:
		model=Quest
		fields=['name', 'location', 'description', 'date']



from django import forms
from registration.forms import RegistrationFormUniqueEmail

class UserProfileRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    image = forms.URLField();

from django import forms
from django.contrib.auth.models import User


# user form for registration
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ["username", "password", "email"]
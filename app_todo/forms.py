from django import forms
from django.forms import PasswordInput
from . models import *

# creating forms
class UserDetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "email", "contact", "password")
        model = UserDetails

class UserLoginForm(forms.ModelForm):
    class Meta:
        fields = ("email", "password")
        model = UserDetails

class UserTodo(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = UserTodo
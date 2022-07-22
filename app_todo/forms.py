from django import forms
from . models import *

# creating forms
class UserDetailsForm(forms.Form):
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "contact")
        model = UserDetails

class UserLoginForm(forms.Form):
    class Meta:
        fields = ("email", "password")
        model = UserDetails

class UserTodo(forms.Form):
    class Meta:
        fields = "__all__"
        model = UserTodo
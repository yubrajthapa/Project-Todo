from django import forms
from app_todo.models import UserDetails, UserTodo

# creating forms
class UserDetailsForm(forms.ModelForm):
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "contact")
        model = UserDetails

class UserLoginForm(forms.ModelForm):
    class Meta:
        fields = ("email", "password")
        model = UserDetails

class UserTodo(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = UserTodo
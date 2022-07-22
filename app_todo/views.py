from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Importing forms to render it in html page
from app_todo.forms import UserDetailsForm, UserLoginForm

# Create your views here.
def index(request):
    return HttpResponse("This is index page ")

def home_page(request):
    return render(request, 'users/homepage.html')

def user_register(request):
    userform = UserDetailsForm()
    context = {
        'form':userform
    }
    return render(request, 'users/register.html', context)
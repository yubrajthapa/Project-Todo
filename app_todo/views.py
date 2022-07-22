from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is index page ")

def home_page(request):
    return render(request, 'users/homepage.html')
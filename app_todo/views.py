from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Importing forms to render it in html page
from .forms import *
from . models import UserDetails

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
    if request.method == "POST":
        # object of models is created.
        userform = UserDetails()
        userform.first_name = request.POST.get('first_name')
        userform.middle_name = request.POST.get('middle_name')
        userform.last_name =request.POST.get('last_name')
        userform.email = request.POST.get('email')
        userform.contact = request.POST.get('contact')
        userform.password = request.POST.get('password')
        userform.save()
        return redirect('/todo/users/login')

    
    return render(request, 'users/register.html', context)

def user_login(request):
    userform = UserLoginForm()
    context = {
        'form':userform
    }
    if request.method =="POST":
        req_email = request.POST.get('email')
        req_pass = request.POST.get('password')
        try:
            std_data = UserDetails.objects.get(email = req_email)
            if std_data.password == req_pass:
                return render(request,'users/homepage.html', context)
            else:
                return render(request,'users/login.html', context)
        except:
            return render(request,'users/login.html',context)


    return render(request, 'users/login.html', context)
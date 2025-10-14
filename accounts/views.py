from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , 'accounts\home.html', {'name': 'John Doe'})

def login_view(request):
    return render(request, 'accounts/login.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')
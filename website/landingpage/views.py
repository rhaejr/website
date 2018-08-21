from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request,'landingpage/home.html')

def login(request):
    return render(request, 'landingpage/login.html')

def register(request):
    return render(request, 'landingpage/register.html')

def forgot_password(request):
    return render(request, 'landingpage/forgot_password.html')

def logout(request):
    return render(request, 'landingpage/home.html')

# def (request):
#     return render(request, 'landingpage/.html')
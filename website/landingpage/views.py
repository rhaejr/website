from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

def messages_alerts(username):
    if not username:
        return {'num_messages': '' , 'num_alerts': ''}
    return {'num_messages': 10 , 'num_alerts': 2}

# Create your views here.
def index(request):
    # request.user.get_username()
    return render(request,'landingpage/home.html', messages_alerts(request.user.get_username()))

def login(request):
    return render(request, 'landingpage/login.html', messages_alerts(request.user.get_username()))

def register(request):
    return render(request, 'landingpage/register.html', messages_alerts(request.user.get_username()))

def forgot_password(request):
    return render(request, 'landingpage/forgot_password.html', messages_alerts(request.user.get_username()))

def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html', messages_alerts(request.user.get_username()))

def user_view(request):
    return render(request, 'landingpage/user.html', messages_alerts(request.user.get_username()))

def ndi(request):
    return render(request, 'landingpage/ndi/ndi.html')

def pt(request):
    return render(request, 'landingpage/ndi/pt.html')
def et(request):
    return render(request, 'landingpage/ndi/et.html')
def ut(request):
    return render(request, 'landingpage/ndi/ut.html')
def mt(request):
    return render(request, 'landingpage/ndi/mt.html')
    
# def (request):
#     return render(request, 'landingpage/.html')
# 
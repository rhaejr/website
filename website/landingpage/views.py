from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from landingpage.models import Exp

def messages_alerts(username):
    if not username:
        return {'num_messages': '' , 'num_alerts': ''}
    return {'num_messages': 10 , 'num_alerts': 2}

# Create your views here.
def index(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect('/user/')
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
    try:
        exp = Exp.objects.filter(method='pt')
        return render(request, 'landingpage/ndi/pt.html', {'exp': exp})
    except Exception as e:
        return render(request, 'landingpage/404.html', {"e" : e})

def et(request):
    try:
        exp = Exp.objects.filter(method='et')
        return render(request, 'landingpage/ndi/et.html', {'exp': exp})
    except Exception as e:
        return render(request, 'landingpage/404.html', {"e" : e})
    
def ut(request):
    try:
        exp = Exp.objects.filter(method='ut')
        return render(request, 'landingpage/ndi/ut.html', {'exp': exp})
    except Exception as e:
        return render(request, 'landingpage/404.html', {"e" : e})

def mt(request):
    try:
        exp = Exp.objects.filter(method='mt')
        return render(request, 'landingpage/ndi/mt.html', {'exp': exp})
    except Exception as e:
        return render(request, 'landingpage/404.html', {"e" : e})
    
# def (request):
#     return render(request, 'landingpage/.html')
# 
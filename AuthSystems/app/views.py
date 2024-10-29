from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponseBadRequest,HttpResponseRedirect,HttpResponse
from .decorators import login_by_ip
# Create your views here.

# 

@login_by_ip
def profile(request):
  user_ip = request.META.get('REMOTE_ADDR')

  return render(request,'app/profile.html',{'ip':user_ip})

# LOCAL_IP = '127.0.0.1'
# LIVE_IP = '<ngrok-public-ip>'
# def local_ip(request):
#     user_ip=request.META.get('REMOTE_ADDR')
#     print('user_ip',user_ip)
#     if user_ip==LOCAL_IP:
#         return render(request,'app/profile.html',{'ip':user_ip})
#     else:
#         return HttpResponseBadRequest('access denied')




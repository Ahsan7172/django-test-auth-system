from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import Signup,Login
from django.contrib import messages
# Create your views here.


def customerregistration(request):
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations!! Registered successfully')
            form.save()
        
            
            # return HttpResponseRedirect('/login/')
    else:
        form=Signup()
    return render(request, 'app/signup.html',{'form':form})

def userLogin(request):
    # if not request.user.is_authenticated:

    if request.method== 'POST':
        fm = Login( data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    else:
        fm = Login()
    return render(request, 'app/login.html', {'form': fm})
def home(request):
    return render(request,'app/home.html')
def dashboard(request):
    return render(request,'app/dashboard.html')
def userlogout(request):
    logout(request)
    return redirect('login')
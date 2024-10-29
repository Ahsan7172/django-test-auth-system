from django.shortcuts import render,redirect,HttpResponse

class MyMiddleware:
    # LOCAL_IP = '127.0.0.1'
    # LIVE_IP = '<ngrok-public-ip>'
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        user_ip=request.META.get('REMOTE_ADDR')
        if user_ip=='127.0.0.1':
            return render(request,'app/profile.html',{'ip':user_ip})
        else:
            return HttpResponse("access denied!")
       
        
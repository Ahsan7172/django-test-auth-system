from django.http import HttpResponse
def login_by_ip(view_func):
    def authorize(request, *args, **kwargs):
        user_ip = request.META.get('REMOTE_ADDR')
        print('user_ip:',user_ip)
        if user_ip=='127.0.0.1':
                return view_func(request,  *args, **kwargs)
        return HttpResponse('access denied!')
    return authorize
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login, logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'thankyou.html')
        else:
            return HttpResponse('Username or Password is incorrect!')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
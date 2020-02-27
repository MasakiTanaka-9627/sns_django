from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        post_username = request.POST['username']
        post_password = request.POST['password']
        try:
            User.objects.get(username=post_username)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(post_username, '', post_password)
            print(request.POST)
        return render(request, 'signup.html', {'some':100})
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        post_username = request.POST['username']
        post_password = request.POST['password']
        user = authenticate(request, username=post_username, password=post_password)
        if user is not None:
            login(request, user)
            return render(request, 'signup')
        else:
            return redirect('login')
    return render(request, 'login.html')

def listfunc(request):
    return render(request, 'list.html')
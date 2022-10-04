from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
    # return HttpResponse('this is  index page')    

def historical(request):
    return render(request, 'historical.html')

def religious(request):
    return render(request, 'religious.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def mostFamous(request):
    return render(request, 'mostFamous.html')


def unpopular(request):
    return render(request, 'unpopular.html')

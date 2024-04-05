from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST['email']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            print(username)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid Employee ID or Password")
            return redirect(user_login)
    return render(request, 'login.html')

def signup(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
      
        
        user = User.objects.create_user(name ,email, password)
        user.save()

        return redirect('user_login')  
    return render(request, 'signup.html')

def homepage(request):
    return render(request, 'home.html')

def jammu(request):
    travellers = travelling_user.objects.filter(place="jammu")
    places = sub_places.objects.filter(main_place = 'jammu')
    return render(request, 'jammu.html',{'travellers':travellers,'places':places})

def booking(request):
    return render(request, 'book.html')

def idukki(request):
    return render(request, 'idukki.html')

def Delhi(request):
    return render(request, 'Delhi.html')

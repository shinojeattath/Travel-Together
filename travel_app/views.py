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

    
    if request.method =='POST':
        
        Travelling_user = travelling_user(
            name=request.POST['name'],
            place=request.POST['place_of_visit'],
            sub_places=request.POST['station'],
            phone=request.POST['contact'],
            date_from=request.POST['date_from'],
            date_to=request.POST['date_to'],
            no_of_travellers=request.POST['num_travelers']
        )
        Travelling_user.save()
        
    return render(request, 'book.html')

def idukki(request):
    return render(request, 'idukki.html')

def Delhi(request):
    return render(request, 'Delhi.html')

def profile(request):
    return render(request, 'profile.html')
from django.shortcuts import render, redirect, get_object_or_404
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
        image = request.FILES['image']
      
        user = User.objects.create_user(name ,email, password)
        user.save()
        image = profile_photo(name=name, photo=image)
        image.save()

        return redirect('user_login')  
    
    return render(request, 'signup.html')

def homepage(request):
    image = profile_photo.objects.all()
    reviews = review.objects.filter(place = 'idukki')

    return render(request, 'home.html',{"image":image, 'reviews':reviews})

def jammu(request):
    username = request.session.get('username')
    travellers = travelling_user.objects.filter(place="jammu")
    places = sub_places.objects.filter(main_place = 'jammu')
    image = profile_photo.objects.all()
    reviews = review.objects.filter(place = 'delhi')

    return render(request, 'jammu.html',{'travellers':travellers,'places':places, 'image':image, 'reviews':reviews})

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
        return redirect(profile)
        
    return render(request, 'book.html')

def idukki(request):
    username = request.session.get('username')
    travellers = travelling_user.objects.filter(place="idukki")
    places = sub_places.objects.filter(main_place = 'idukki')
    image = profile_photo.objects.all()
    reviews = review.objects.filter(place = 'idukki')

    return render(request, 'idukki.html',{'travellers':travellers, 'places':places, 'image':image, 'reviews':reviews})

def Delhi(request):
    username = request.session.get('username')
    travellers = travelling_user.objects.filter(place="delhi")
    places = sub_places.objects.filter(main_place = 'delhi')
    image = profile_photo.objects.all()
    reviews = review.objects.filter(place = 'delhi')

    return render(request, 'Delhi.html',{'travellers':travellers,'places':places, 'image':image, 'reviews':reviews})

def profile(request):
    username = request.session.get('username')
    booked = travelling_user.objects.filter(name=username)
    try:
        image = profile_photo.objects.get(name=username)
    except profile_photo.DoesNotExist:
        image = None

    return render(request, 'profile.html', {'booked':booked, 'username':username, 'image':image})

def cancelFunc(request):
    username = request.session.get('username')
    booked = get_object_or_404(travelling_user, name = username)
    booked.delete()
    return redirect('profile')

def reviewpage(request):

    username = request.session.get('username')
    photo = profile_photo.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        written_review = request.POST['written_review']
        reviews = review(name=name, place=place, review=written_review)
        reviews.save()
        return redirect('homepage')
    
    return render(request, 'reviewpage.html', {'username':username, 'photo':photo})

   

def remainder(request):
    return render(request, 'remainder.html')

def newremainder(request):
    return render(request, 'newrem.html')

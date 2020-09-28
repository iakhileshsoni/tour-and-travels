from django.shortcuts import render, redirect
# for working on registration and login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from travel.models import Destination
from travel.models import Traveller # importing model classs for showing the student from the Database


# Create your views here.
def home(request):
    destinations = Destination.objects.all()
    return render(request, 'travel/index.html', {'destinations': destinations})


def travellers(request):
    travellers = Traveller.objects.all()
    return render(request, 'travel/travellers.html', {'travellers':travellers})


def about(request):
    response = render(request, 'travel/about.html')
    return response


# Regrstration form for Travello
def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        gender = request.POST['gender']
        image = request.FILES['image']  # Required to use FILES[] while working with Image
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is taken already")
            else:
                traveller = Traveller.objects.create(firstname=firstname, lastname=lastname, email=email,
                    gender=gender, password=password, image=image)
                print("Traveller is Saved")
                return redirect('/')
        else:
            messages.info(request, "Password is not matching")
            return redirect('travel/register.html')
        return redirect('/')
    else:
        return render(request, 'travel/register.html')


# Login Page for the Travello
def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'travel/login.html')



def contact(request):
    response = render(request, 'travel/contact.html')
    return response


def logout(request):
    auth.logout(request)
    return redirect('/')

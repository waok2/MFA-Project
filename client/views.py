from django.shortcuts import render, redirect
from .models import Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def home(request):
    return render(request, 'client/home.html')




def register(request):
    if request.method == 'POST' :

        if request.POST['surname'] and request.POST['other_names'] and request.POST['national_id'] and request.POST['cell_number'] and request.POST['branch'] and request.POST['business_area'] and request.POST['occupation'] and request.POST['status'] :
            client1 = Client()
            client1.surname = request.POST['surname']
            client1.other_names = request.POST['other_names']
            client1.national_id = request.POST['national_id']
            client1.cell_number = request.POST['cell_number']
            client1.branch = request.POST['branch']
            client1.business_area = request.POST['business_area']
            client1.occupation = request.POST['occupation']
            client1.status = request.POST['status']
            client1.pub_date = timezone.datetime.now()
            client1.creator = request.user
            client1.save()

            return redirect('home')
        else :
            return render(request, 'client/register.html', {'error':'All fields are required'})

    else :
        return render(request, 'client/register.html')


def login(request):

    if request.POST['username'] and request.POST['password']:

        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])


        return render(request, 'client/login.html')

    else:
        return render(request, 'client/login.html')

def all(request):
    return render(request, 'client/all.html')


def main(request):
    return render(request, 'client/main.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import  login_required


# Create your views here.

@login_required(login_url='/client/login')
def home(request):
    clients = Client.objects.all()
    return render(request, 'client/home.html', {'clients':clients})

@login_required(login_url='/client/login')
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

            #return redirect('/client/' + str(client1.pk))
            return redirect('home')
        else :
            return render(request, 'client/register.html', {'error':'All fields are required'})

    else :
        return render(request, 'client/register.html')


def login(request):

   # if request.POST['username'] and request.POST['password']:
    if request.method == 'POST' :
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('landing')
        else:
            return render(request, 'client/login.html', {'error':'username or password is incorrect'})

    else:
        return render(request, 'client/login.html')


def logout(request):
    
    if request.method == 'POST' :
        auth.logout(request)
        return redirect ('home')
    else:
        return render(request, 'client/login.html')


@login_required(login_url='/client/login')
def all(request):
    return render(request, 'client/all.html')


@login_required(login_url='/client/login')
def main(request):
    return render(request, 'client/main.html')


@login_required(login_url='/client/login')
def client(request, client_id):
    client = get_object_or_404(Client, pk= client_id)
    return render(request, 'client/client.html', {'client':client})


@login_required(login_url='/client/login')
def landing(request):
    return render(request, 'client/landing.html')

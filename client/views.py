from django.shortcuts import render


# Create your views here.


def home(request):

    #client = client.objects
    client = 'client working'
    return render(request, 'client/home.html', {'client': client})


def register(request):
    return render(request, 'client/register.html')
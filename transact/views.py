from django.shortcuts import render

# Create your views here.


def paydashboard(request):
    return render(request, 'transact/paydashboard.html')


def newloan(request):
    return render(request, 'transact/newloan.html')


def newpay(request):
    return render(request, 'transact/newpay.html')

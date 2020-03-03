from django.shortcuts import render, redirect
from .models import loan, pay
from django.utils import timezone
from client.models import client



def paydashboard(request):
    return render(request, 'transact/paydashboard.html')


def newloan(request):

    client1= client.objects.all()


    if request.method == 'POST':

        if request.POST['client'] and request.POST['amount'] and request.POST['repay_amount'] and request.POST['cycles'] and request.POST['current_amount'] and request.POST['mode_cycles'] and request.POST['status']:
            loan1 = loan()


            #client2 = client.objects.only(request.POST['client']).get(id=client['client_id'])
           # client_testing = client2.request.GET.get("q")
            client_instance = client.objects.get(id=request.POST['client'])
            loan1.client_id = client_instance
            loan1.amount = request.POST['amount']
            loan1.repay_amount = request.POST['repay_amount']
            loan1.cycles = request.POST['cycles']
            loan1.current_amount = request.POST['current_amount']
            loan1.mode_cycles = request.POST['mode_cycles']
            loan1.status = request.POST['status']
            loan1.pub_date = timezone.datetime.now()
            loan1.creator = request.user
            loan1.save()

            return redirect('paydashboard')
        else:
            return render(request, 'transact/newloan.html', {'error': 'All fields are required'})

    else :
        return render(request, 'transact/newloan.html', {'clients':client1})




def newpay(request):
    loan1 = loan.objects.all()

    if request.method == 'POST':

        if request.POST['loan_id'] and request.POST['amount'] and request.POST['cycles'] and request.POST['mode_of_payment']:
            loan_instance = loan.objects.get(id=request.POST['loan_id'])
            pay1 = pay()
            pay1.loan_id = loan_instance
            pay1.amount = request.POST['amount']
            pay1.cycles = request.POST['cycles']
            pay1.mode_of_payment = request.POST['mode_of_payment']
            pay1.creator = request.user
            pay1.pub_date = timezone.datetime.now()
            pay1.save()

            return redirect('paydashboard')
        else:
            return render(request, 'transact/newpay.html', {'error': 'All fields are required'})


    else:
        return render(request, 'transact/newpay.html',{'loans':loan1})

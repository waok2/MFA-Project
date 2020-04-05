from django.shortcuts import render, redirect, get_object_or_404
from .models import Loan, Pay
from django.utils import timezone
from client.models import Client
from django.contrib.auth.decorators import login_required


@login_required(login_url='/client/login')
def paydashboard(request):
    return render(request, 'transact/paydashboard.html')


@login_required(login_url='/client/login')
def newloan(request):

    client1= Client.objects.all()


    if request.method == 'POST':

        if request.POST['client'] and request.POST['amount'] and request.POST['repay_amount'] and request.POST['cycles'] and request.POST['current_amount'] and request.POST['mode_cycles'] and request.POST['status']:
            loan1 = Loan()


            #client2 = client.objects.only(request.POST['client']).get(id=client['client_id'])
           # client_testing = client2.request.GET.get("q")
            client_instance = Client.objects.get(id=request.POST['client'])
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
            return render(request, 'transact/newloan.html', {'error': 'All fields are required', 'clients': client1})

    else :
        return render(request, 'transact/newloan.html', {'clients':client1})


@login_required(login_url='/client/login')
def newpay(request):
    loan1 = Loan.objects.all()

    if request.method == 'POST':

        if request.POST['loan_id'] and request.POST['amount'] and request.POST['cycles'] and request.POST['mode_of_payment']:
            loan_instance = Loan.objects.get(id=request.POST['loan_id'])
            pay1 = Pay()
            pay1.loan_id = loan_instance
            pay1.amount = request.POST['amount']
            pay1.cycle = request.POST['cycles']
            pay1.mode_of_payment = request.POST['mode_of_payment']
            pay1.creator = request.user
            pay1.pub_date = timezone.datetime.now()
            pay1.save()

            return redirect('paydashboard')
        else:
            return render(request, 'transact/newpay.html', {'error': 'All fields are required', 'loans': loan1})


    else:
        return render(request, 'transact/newpay.html', {'loans':loan1})


@login_required(login_url='/client/login')
def loans(request):

    loans_all = Loan.objects.all()
    clients_all = Client.objects.all()
    #loan_record = {}  
   


    return render(request, 'transact/loans.html', {'loans_all':loans_all, 'clients_all':clients_all})


@login_required(login_url='/client/login')
def payments(request):

    payments_all = Pay.objects.all()

    return render(request, 'transact/payments.html', {'payments_all':payments_all})


@login_required(login_url='/client/login')
def loan(request,loan_id):

   loan = get_object_or_404(Loan, pk=loan_id)
   #client = loan.client
   client = get_object_or_404(Client, loan=loan_id)
   return render(request, 'transact/loan.html', {'loan': loan, 'client':client})

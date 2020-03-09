from django.db import models
from django.contrib.auth.models import User
from client.models import Client



class Loan(models.Model):

    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
    amount = models.IntegerField()
    repay_amount = models.IntegerField()
    cycles = models.IntegerField()
    current_amount = models.IntegerField()
    mode_cycles= models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    pub_date = models.DateTimeField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __int__(self):
        return self.client_id

   



    


class Pay(models.Model):

    loan_id = models.ForeignKey(Loan, on_delete=models.PROTECT)
    amount = models.IntegerField()
    cycle = models.IntegerField()
    mode_of_payment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.mode_of_payment

   




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

    def __str__(self):
        return self.mode_cycles

    class Meta:
        ordering = ['mode_cycles']



    


class Pay(models.Model):

    loan_id = models.ForeignKey(Loan, on_delete=models.PROTECT)
    amount = models.IntegerField()
    cycles = models.IntegerField()
    mode = models.CharField(max_length=255)
    pub_date = models.DateTimeField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.mode

    class Meta:
        ordering = ['pub_date']




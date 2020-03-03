from django.db import models
from django.contrib.auth.models import User
from client.models import client



class loan(models.Model):

    client_id = models.ForeignKey(client, on_delete=models.PROTECT)
    amount = models.IntegerField()
    repay_amount = models.IntegerField()
    cycles = models.IntegerField()
    current_amount = models.IntegerField()
    mode_cycles= models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    pub_date = models.DateTimeField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.client_id

    class Meta:
        ordering = ['client_id']



    


class pay(models.Model):

    loan_id = models.ForeignKey(loan, on_delete=models.PROTECT)
    amount = models.IntegerField()
    cycles = models.IntegerField()
    mode = models.CharField(max_length=255)
    pub_date = models.DateTimeField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.loan_id

    class Meta:
        ordering = ['loan_id']




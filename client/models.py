from django.db import models
from django.contrib.auth.models import User

#Create your models here.


class Client(models.Model):
   
    surname = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255)
    national_id = models.IntegerField()
    cell_number = models.IntegerField()
    branch= models.CharField(max_length=255)
    business_area = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    #body = models.TextField()
    pub_date = models.DateTimeField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.surname


    class Meta:
            ordering = ['surname']


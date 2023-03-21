from django.db import models
import uuid
class Tickets(models.Model): #Table to store Reservations while booking tickets.
    pnr=models.AutoField(unique=True,primary_key=True)
    transactionid = models.UUIDField( default=uuid.uuid4, editable=False)
    email=models.CharField(max_length=100,default="test@test.com")
    trainno=models.IntegerField()
    trainname=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    kms=models.IntegerField()
    classs=models.CharField(max_length=5)
    doj=models.CharField(max_length=15)
    amt=models.IntegerField()
    passno=models.IntegerField()
    list1=models.CharField(max_length=500)
# Create your models here.
# Aarsh Saxena (21bec001)

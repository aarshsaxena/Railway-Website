from django.db import models
import uuid

class Train(models.Model): #Table to store traindata.
    trainno=models.IntegerField(primary_key=True, unique=True)
    trainname=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    depart=models.CharField(max_length=5)
    arrival=models.CharField(max_length=5)
    kms=models.IntegerField()
    ec=models.IntegerField()
    cc=models.IntegerField()

class Station(models.Model): #Table to store station data.
    station=models.CharField(unique=True, max_length=30)

class Website(models.Model): #Table to store Website
    title=models.CharField(unique=True,max_length=100)
    
# Create your models here.
#Aarsh Saxena (21bec001)

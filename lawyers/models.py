from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Lawyers(models.Model):
    Name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    Location = models.CharField(max_length=100)
    Lawyer_Qualification = models.CharField(max_length=200)
    noOfViews = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    profileUrl = models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.Name

class LawyerSpecilization(models.Model):
    Lawyer = models.ForeignKey(Lawyers,on_delete=models.SET_NULL,null=True)
    fees = models.IntegerField()
    SpecilizationType = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    raitings = models.IntegerField(default=0)

    def __str__(self):
        return self.Lawyer.Name

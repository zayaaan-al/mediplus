from django.db import models

# Create your models here.
class doctordetails(models.Model):
    doctorphoto = models.ImageField()
    doctorname = models.CharField(max_length=50)
    doctoremail = models.CharField(max_length=50)
    doctorphone = models.IntegerField(max_length=50)
    doctorspecification = models.CharField(max_length=50)
    doctorfees = models.CharField(max_length=50)
    
    

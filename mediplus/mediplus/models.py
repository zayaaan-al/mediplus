from django.db import models

class userdetailss(models.Model):
    userphoto = models.ImageField()
    username = models.CharField(max_length=50)
    useremail = models.CharField(max_length=50)
    userphone = models.IntegerField(max_length=50)
    userpassword = models.CharField(max_length=50)
    userage = models.CharField( max_length=50)
   
    

    
    


    

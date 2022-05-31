from django.db import models

from app.models import cource3


class users(models.Model):
    userid=models.AutoField(primary_key=True)
    courceid=models.ForeignKey(cource3, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=500, default='', null=True)
    lastname=models.CharField(max_length=200, default='', null=True)
    username=models.CharField(max_length=200, default='', null=True)
    email=models.EmailField(max_length=200, default='', null=True)
    password=models.CharField(max_length=200, default='', null=True)
    courcenames=models.CharField(max_length=200, default='', null=True)



# class userdetails(models.Model):
#     userid=models.AutoField(primary_key=True)
#     courceid=models.ForeignKey(cource3, on_delete=models.CASCADE)
#     firstname=models.CharField(max_length=500, default='', null=True)
#     lastname=models.CharField(max_length=200, default='', null=True)
#     username=models.CharField(max_length=200, default='', null=True)
#     email=models.EmailField(max_length=200, default='', null=True)
#     password=models.CharField(max_length=200, default='', null=True)
#     courcenames=models.CharField(max_length=200, default='', null=True)
#     courselevel=models.CharField(max_length=200, default='', null=True)
   

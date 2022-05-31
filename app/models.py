from django.db import models
from django.contrib.auth.models import User


class platform(models.Model):
    platformid=models.AutoField(primary_key=True)
    id=models.ForeignKey(User, on_delete=models.CASCADE)
    platformname=models.CharField(max_length=255, default='', null=True)
    platformdsp=models.CharField(max_length=2055, default='', null=True)


class cource3(models.Model):
    courceid=models.AutoField(primary_key=True)
    id=models.ForeignKey(User, on_delete=models.CASCADE)
    platformid=models.ForeignKey(platform, on_delete=models.CASCADE)
    courcenames=models.CharField(max_length=200, default='', null=True)
    coursedsp=models.CharField(max_length=200, default='', null=True)
    coursemodules=models.CharField(max_length=200, default='', null=True)
    courselevel=models.CharField(max_length=200, default='', null=True)
    

class tutorial(models.Model):
    tutorialid=models.AutoField(primary_key=True)
    id=models.ForeignKey(User, on_delete=models.CASCADE)
    courceid=models.ForeignKey(cource3, on_delete=models.CASCADE)
    videoname=models.CharField(max_length=200, default='', null=True)
    videodsp=models.CharField(max_length=2000, default='', null=True)
    videos=models.FileField(upload_to='video', null=True)




class questions(models.Model):
    questionsid=models.AutoField(primary_key=True)
    id=models.ForeignKey(User, on_delete=models.CASCADE)
    tutorialid=models.ForeignKey(tutorial, on_delete=models.CASCADE)
    courceid=models.ForeignKey(cource3, on_delete=models.CASCADE)
    question=models.CharField(max_length=500, default='', null=True)
    option1=models.CharField(max_length=200, default='', null=True)
    option2=models.CharField(max_length=200, default='', null=True)
    option3=models.CharField(max_length=200, default='', null=True)
    answers=models.CharField(max_length=200, default='', null=True)

from django.shortcuts import redirect, render
import email
from unicodedata import name

from app.models import cource3
from app.models import  questions
from app.models import  tutorial

from .models import *

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from .forms import * 
from django.contrib import messages

def loginuser(request):
    return render(request, 'loginuser.html')

def signinuser(request):
    creg=cource3.objects.all()
    return render(request, 'signin.html', {"cource3": creg})



def signup2(request):
    try:
        if request.method=='POST':
            fname=request.POST['first_name']
            lname=request.POST['last_name']
            uname=request.POST['username']
            uemail=request.POST['email']
            c_name=request.POST["courcename"]
            creg=cource3.objects.get(courcenames=c_name)
            upassword=request.POST['password']
            uconfirmpassword=request.POST['cpassword']
            # platform_name=request.POST["platformname"]

            if upassword==uconfirmpassword:
                # if users.objects.filter(uname=uname):
                #     messages.success(request, 'The Username is Already Exist')
                if users.objects.filter(username=uname):
                    return redirect('loginuser')
                else:
                    user=users(firstname=fname, lastname=lname, username=uname, email=uemail, password=upassword, courceid=creg,courcenames=c_name)
                    user.save()
                    return redirect('loginuser')
    except:
        return redirect('signinuser')

        
def login2(request):
    try:

        if request.method=='POST':
            userd=users.objects.get(username=request.POST['username'],password=request.POST['password'])
            request.session['username']=userd.username
            
            return redirect('firstpage')
    except users.DoesNotExist as e:
        messages.success(request, 'username or password is invalid')
        return redirect('loginuser')

    


def firstpage(request):
    userdetail=users.objects.get(username=request.session['username'])
    cources=cource3.objects.get(courcenames=userdetail.courcenames)

    return render(request, 'first.html', {'userdetail': userdetail, "cource3": cources})

        


    


def secondpage(request):
    userdetail=users.objects.get(username=request.session['username'])
    cources=cource3.objects.get(courcenames=userdetail.courcenames)
    
    tutorials1=tutorial.objects.filter(courceid=cources.courceid)
    exam = questions.objects.filter(courceid=cources.courceid)
   
    return render(request,"second.html", {'userdetail': userdetail, "cource3": cources,"tutorial": tutorials1, "questions": exam})

# def tutorialpage(request):
#     userdetail=users.objects.get(username=request.session['username'])
#     cources=cource3.objects.get(courcenames=userdetail.courcenames)
#     tutorials1=tutorial.objects.filter(courceid=cources.courceid)
   
    
#     return render(request, 'video.html', {'userdetail': userdetail, "cource3": cources, "tutorial": tutorials1})


def certi(request):
    userdetail=users.objects.get(username=request.session['username'])
    cources=cource3.objects.get(courcenames=userdetail.courcenames)

    return render(request, 'certificate.html', {'userdetail': userdetail, "cource3": cources})



def pro(request):
    userdetail=users.objects.get(username=request.session['username'])
    cources=cource3.objects.get(courcenames=userdetail.courcenames)

    return render(request, 'pro.html', {'userdetail': userdetail, "cource3": cources})


# def tutorialselection(request):
#     userdetail=users.objects.get(username=request.session['username'])
#     cources=cource3.objects.get(courcenames=userdetail.courcenames)
#     tutorials1=tutorial.objects.filter(courceid=cources.courceid)
#     return render(request, 'videosection.html', {'userdetail': userdetail, "cource": cources, "tutorial": tutorials1})


def  tutorialpage(request):
    userdetail=users.objects.get(username=request.session['username'])
    cources=cource3.objects.get(courcenames=userdetail.courcenames)
    tutorials1=tutorial.objects.filter(courceid=cources.courceid)
    return render(request, 'video.html', {'userdetail': userdetail, "cource": cources, "tutorial": tutorials1})

def tutorialselection(request, tutorialid):
    tutorials1=tutorial.objects.filter(tutorialid=tutorialid)
    return render(request, 'videosection.html', { 'tutorial': tutorials1})
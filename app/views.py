from django.shortcuts import redirect, render
import email
from unicodedata import name

from .models import *

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required 
from django.contrib import messages



def loginadmin(request):
    return render(request, 'loginadmin.html')

def signinadmin(request):
    return render(request, 'signinadmin.html')



def signup(request):
    try:
        if request.method == 'POST':
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            confirmpassword=request.POST['cpassword']

            if password==confirmpassword:
                if User.objects.filter(username=username):
                    messages.success(request, 'The Username is Already Exist')
                    return redirect('signinadmin')
                else:
                    user=User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email , password=password)
                    user.save()
                    return redirect('loginadmin')
    except:
        return redirect('signinadmin')

        
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        request.session['username']=user.username
        if user is not None:
            auth.login(request, user)
            return redirect('dash')
        else:
            messages.info(request, 'INVALID USERNAME OR PASSWORD')
            return redirect('loginadmin')
    
def dash(request):
    return render(request, 'dash.html')

def platform1(request):
    return render(request, 'platform.html')

def addplatform(request):
    user=User.objects.all()
    return render(request, 'addplatform.html')


def register(request):
    if request.method=="POST":
        p_name=request.POST["pname"]
        p_dsp=request.POST["pdsp"]
        user=User.objects.get(username=request.session['username'])
        platforms=platform(platformname=p_name, platformdsp=p_dsp, id=user)
        platforms.save()
        
        return redirect('show')
    else:
        return redirect('addplatform')

    




def show(request):
    user=User.objects.get(username=request.session['username'])
    platforms=platform.objects.filter(id=user)
    return render(request, 'platform.html', {'platform':platforms})



def edit(request, platformid):
    user=User.objects.get(username=request.session['username'])
    platforms=platform.objects.filter(id=user)
    platforms=platform.objects.get(platformid=platformid)
    return render(request, 'edit.html', {'platform':platforms})

def update(request, platformid):
    try:
        if request.method=="POST":
            platforms=platform.objects.get(platformid=platformid)
            user=User.objects.get(username=request.session['username'])
            platforms.platformname=request.POST.get('pname')
            platforms.platformdsp=request.POST.get('pdsp')
            platforms.save()
            return redirect('show')
    except:
        return redirect('addplatform')


def delete(request, platformid):
    platforms=platform.objects.get(platformid=platformid)
    platforms.delete()
    return redirect('show')





def cources(request):
    return render(request, 'cource.html')




def cadd(request):
    user=User.objects.all()
    user=User.objects.get(username=request.session['username'])
    platforms=platform.objects.filter(id=user)
    return render(request, 'cadd.html', {"platform": platforms })





def register2(request):
    if request.method=="POST":
        c_name=request.POST["cname"]
        c_dsp=request.POST["cdsp"]
        c_mod=request.POST["cmod"]
        c_level=request.POST["clevel"]
        c_id=request.POST["pname"]
        user=User.objects.get(username=request.session['username'])
        platforms=platform.objects.get(platformname=c_id)
        creg=cource3(courcenames=c_name, coursedsp=c_dsp,  coursemodules=c_mod,courselevel=c_level, platformid=platforms, id=user)
        creg.save()
        
        
        return redirect('cshow')
    else:
        return redirect('cadd')

def cshow(request):
    user=User.objects.get(username=request.session['username'])
    creg=cource3.objects.filter(id=user)
    return render(request, 'cource.html', {'cource':creg})

def editcource(request, courceid):
    user=User.objects.get(username=request.session['username'])
    platforms=platform.objects.filter(id=user)
    creg=cource3.objects.get(courceid=courceid)
    return render(request,'editcource.html',{'cource3':creg, 'platform':platforms})

def deletecource(request,  courceid):
    creg=cource3.objects.get( courceid= courceid)
    creg.delete()
    return redirect('cshow')

def update2(request,  courceid):
   
        if request.method=="POST":
            user=User.objects.get(username=request.session['username'])
            creg=cource3.objects.get(courceid= courceid,)
            creg.courcenames=request.POST.get('cname')
            creg.coursedsp=request.POST.get('cdsp')
            creg.coursemodules=request.POST.get('cmod')
            creg.courselevel=request.POST.get('clevel')
            platforms=platform.objects.all()
            platforms.pname=request.POST.get('pname')
            creg.save()
            
            
            return redirect('cshow')




def tadd(request):
    user=User.objects.all()
    user=User.objects.get(username=request.session['username'])
    creg=cource3.objects.filter(id=user)
    return render(request, 'tadd.html', {"cource3": creg})

def register3(request):
    if request.method=="POST":
        v_name=request.POST["vname"]
        v_dsp=request.POST["vdsp"]
        t_id=request.POST["cname"]
        user=User.objects.get(username=request.session['username'])
        creg=cource3.objects.get(courcenames=t_id)
        v_video=request.FILES["video1"]
       
        treg=tutorial(videoname=v_name, videodsp=v_dsp, videos=v_video, courceid=creg, id=user)
        treg.save()
        
        
        return redirect('tshow')
    else:
        return redirect('tadd')


def tshow(request):
    user=User.objects.get(username=request.session['username'])
    treg=tutorial.objects.filter(id=user)
    return render(request, 'tshow.html', {'tutorial':treg})


def delete1(request,tutorialid):
    treg=tutorial.objects.get(tutorialid=tutorialid)
    treg.delete()
    return redirect('tshow')

def tedit(request, tutorialid):
    user=User.objects.get(username=request.session['username'])
    creg=cource3.objects.filter(id=user)
    treg=tutorial.objects.get(tutorialid=tutorialid)
   
    return render(request,'tedit.html',{'cource3':creg, 'tutorial':treg})

def update3(request, tutorialid):
   
        if request.method=="POST":
            user=User.objects.get(username=request.session['username'])
            treg=tutorial.objects.get(tutorialid=tutorialid)
            treg.videoname=request.POST.get('vname')
            treg.videodsp=request.POST.get('vdsp')
            try:
                treg.videos=request.FILES['video1']
            except:
                pass
            creg=cource3.objects.all()
            creg.courcenames=request.POST.get('cname')
            treg.save()
            return redirect('tshow')



def qa(request):
    user=User.objects.all()
    user=User.objects.get(username=request.session['username'])
    creg=cource3.objects.filter(id=user)
    treg=tutorial.objects.filter(id=user)
    return render(request, 'qa.html', {'tutorial':treg , 'cource3': creg})


    

def register4(request):
    if request.method=="POST":
        q_name=request.POST["questionsname"]
        q_answer=request.POST["ans"]
        q_id=request.POST["vname"]
        op1=request.POST["op1"]
        op2=request.POST["op2"]
        op3=request.POST["op3"]
        c_name=request.POST["cname"]
        user=User.objects.get(username=request.session['username'])
        treg=tutorial.objects.get(videoname=q_id)
        creg=cource3.objects.get(courcenames=c_name)
        qreg=questions(question=q_name,answers=q_answer,tutorialid=treg, option1=op1, option2=op2, option3=op3, courceid=creg, id=user )
        qreg.save()
        
        
        return redirect('qashow')
    else:
        return redirect('qa')


def qashow(request):
    user=User.objects.get(username=request.session['username'])
    qreg=questions.objects.filter(id=user)
    return render(request, 'qashow.html', {'questions':qreg})


def deleteq(request,  questionsid):
    qreg=questions.objects.get(questionsid= questionsid)
    qreg.delete()
    return redirect('qashow')


def logout(request):
    auth.logout(request)
    return redirect('base')


    
import imp
from django.shortcuts import redirect, render




def app(request):
    return redirect('/app/')

def app2(request):
    return redirect('/app2/')

def base(request):
    return render(request, 'base.html')



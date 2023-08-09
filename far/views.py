from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import farmer

def home(request):
    return render(request,'index.html')
def org(request):
    return render(request,'organic.html')
def chem(request):
    return render(request,'chemical.html')
def story(request):
    return render(request,'story.html')
def about(request):
    return render(request,'about.html')
def want(request):
    return render(request,'want.html')

def cont(request):
    return render(request,'contact.html')
def form1(request):
    if request.method=='POST':
        
        e=farmer.objects.create(name=request.POST['name'],address=request.POST['add'],email=request.POST['email'],product=request.POST['pname'],type=request.POST['ptype'],doc=request.POST['textarea'])
        e.save()
        return render(request,'submit.html')
    else:
        return redirect("/")
        # return redirect("/")
def find(request):
    e=farmer.objects.all()
    return render(request,'find.html',{'hh':e})
        
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
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

def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")

def filllogin(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['uname'],password=request.POST["psw"])
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Please enter valid details")
            return render(request,"login.html")
    else:

        return render(request,"login.html")

def fillregister(request):
    if request.method=="POST":
        if User.objects.filter(username=request.POST["uname"]).exists():
            messages.error(request,"Username already exist")
            return render(request,"register.html")
        if User.objects.filter(email=request.POST["email"]).exists():
            messages.error(request,"Email already exist")
            return render(request,"register.html")
        if(request.POST["psw1"]!=request.POST["psw2"]):
            messages.error(request,"Pls repeat the password correctly")
            return render(request,"register.html")
        
        x=User.objects.create_user(username=request.POST["uname"],email=request.POST["email"],first_name=request.POST["fname"],last_name=request.POST["lname"],password=request.POST["psw1"])
        messages.success(request,"Hurray .... Successfull Registered to Farmword!")
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

        
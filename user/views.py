from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from user.forms import RegistrationForm,LoginForm

def register(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"user/login.html")

    return render(request,"user/registration.html",context)


def signin(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"user/home.html")
            else:
                return render(request,"user/login.html",context)
    return render(request,"user/login.html",context)
def signout(request):
    logout(request)
    return redirect("signin")
def editprofile(request):
    user=User.objects.get(username=request.user)
    form=RegistrationForm(instance=user)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        context["form"]=form
        return render(request, "user/editprofile.html", context)
    return render(request,"user/editprofile.html",context)

def userHome(request):
    return render(request,"user/home.html")

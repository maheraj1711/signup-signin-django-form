from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import*

def signup(request):
    if request.method=="POST":
        form=usersignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form=usersignupForm()
    return render(request,'signup.html',{'form':form})
    
def signin(request):
    if request.method=="POST":
        form=signInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
    else:
        form=signInForm()
    return render(request,'signin.html',{'form':form})


def logedout(request):
    logout (request)
    return redirect('signin')

def home(request):
    return render(request,'home.html')



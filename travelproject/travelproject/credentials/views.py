from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout


# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,"login.html")
def logout1(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

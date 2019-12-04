from django.shortcuts import render, redirect
from .models import registration
from .forms import formreg
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
# from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'index.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')
    
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save();
                print('user created')
                return redirect('signin')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')






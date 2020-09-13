from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from .models import AddUser
#from django.core.mail import send_mail
#from random import randint
from django.conf import settings
# Create your views here.
def index(request):
        return render(request,'app1/index.html')



def login(request):
    if request.session.get('username'):
        return render(request,"app1/dashboard.html")
        
    else:
        form = Login()
        return render(request,"app1/login.html",{'form':form})

def signup(request):
    form = Signup()
    return render(request,"app1/signup.html",{'form':form})

def signup1(request):
    form = Signup(request.POST,request.FILES)
    if form.is_valid():
        if request.method == "POST":
            pswd = form.cleaned_data['password']
            cpswd = form.cleaned_data['confirm_password']
            if pswd == cpswd:
                dict = {
                    'firstname' : form.cleaned_data['firstname'],
                    'lastname' : form.cleaned_data['lastname'],
                    'username' : form.cleaned_data['username'],
                    'email' : form.cleaned_data['email'],
                    'password' : form.cleaned_data['password'],
                    'mobileno' : form.cleaned_data['mobileno'],
                } 
                new_user = AddUser.objects.create(**dict)
                new_user.save()
                return render(request,"app1/login.html")
            else:
                error = "Password does not match...Try again"
                form = Signup()
                return render(request,"app1/signup.html",{'form':form,'error':error})
        else:
            error = "Invalid method"
            form = Signup()
            return render(request,"app1/signup.html",{'form':form,'error':error})
    else:
        error = "Invalid method"
        form = Signup()
        return render(request,"app1/signup.html",{'form':form,'error':error})

def login1(request):
    form = Login(request.POST)
    if form.is_valid():
        if request.method == "POST":
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = AddUser.objects.get(username=username)
            except AddUser.DoesNotExist as e:
                error = "No such user...Signup to login"
                form = Login()
                return render(request,"app1/login.html",{'error':error,'form':form})
            else:
                pswd = user.password
                if password == pswd:
                    request.session['username'] = username
                    return render(request,"app1/dashboard.html")
                else:
                    error = "Password does not matched.."
                    form = Login()
                    return render(request,"app1/login.html",{'error':error,'form':form})
                    
            #return HttpResponse("User with {} logged in".format(email))
        else:
            error = "INVALID METHOD"
            form = Login()
            return render(request,"app1/login.html",{'form':form})
    else:
        error = "Invalid form"
        form = Login()
        return render(request,"app1/login.html",{'form':form})

def logout(request):
    del request.session['username']
    form = Login()
    return render(request,"app1/login.html",{'form':form})

def contact(request):
    return render(request,'app1/contact.html')

def profile(request):
    user = request.session['username']
    args = AddUser.objects.filter(username__exact=user)
    data = []
    for var in args:
        d = {
            'firstname' : var.firstname,
            'lastname' : var.lastname,
            'email' : var.email,
            'mobileno' : var.mobileno,
            'username' : var.username,
            'password' : var.password
        }
        data.append(d)
    return render(request,"app1/profile.html",{'data':data})
    
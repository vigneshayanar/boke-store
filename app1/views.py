from django.shortcuts import render,redirect
from . models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from email.message import EmailMessage
import ssl
import smtplib
import random
from django .conf import settings
from django.core.cache import cache
# Create your views here.
def home(request):
    product=Product.objects.all()
    return render(request,'app1/home.html',{'product':product})

def about(request):
    return render(request,'app1/about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error. Please check your username and password.")
            return redirect('login')

    return render(request, 'app1/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"you have been looged out...!")
    return redirect('home')

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            user=User.objects.create_user(name,email,pass1)
            messages.success(request,"you have been registered")
            return redirect('home')
        else:
            messages.success(request,"error in registration check password")
            return redirect('register')

    return render(request,'app1/resgister.html')


def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'app1/product.html',{'product':product})

def otp(request):
    if request.method=="POST":
        to=request.POST.get('email')
        generate_otp(request,to)
        return redirect('otpverify')
    else:
        return render(request,'app1/otp.html')

def generate_otp(request,to):
    number=random.randint(1000,9999)
    email_sender="Vigneshayanar@gmail.com"
    email_password="lrbt pvnt lwrd kshk"
    email_receiver=to
    subject="your oto for Byers"
    body = "Welcome to Buyers! Your OTP is: {}".format(number)
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.send_message(em)
    cache.set(number,True,timeout=300)
    print(number)
    

def verifyotp(request):
    if request.method=="POST":
        verify=request.POST.get("otpverify")
        stored_value=cache.get(verify)
        if stored_value:
            cache.delete(verify) 
            return redirect('home')
        else:
            print('hi')
            return redirect('otp')
    else:
        return render(request,'app1/otpverify.html')


                
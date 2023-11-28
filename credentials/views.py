from django.contrib import messages ,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken !")
                print("Username already taken !")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exist !")
                print("Email already Exist !")
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                            password=password)
                user.save()
                print("User %s has been created" % username)
                messages.info(request, "User %s has been created" % username)
                return redirect('login')
        else:
            print("Passwords didn't match !")
            messages.info(request, "Passwords didn't match !")
            return render(request, "register.html")
        # return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import auth
from . models import extendedUser
# from django.contrib.auth.decorators import login_required


# Create your views here.


def dr_dashboard(request):
    # data = extendedUser.objects.filter(user=request.user)
    return render(request,'doctor/dashboard.html')

def dr_SignUp_Page(request):
    if request.method == "POST":
        # to create new user
        if request.POST['password'] == request.POST['re_password']:
            #both the passwords matched
            #now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'doctor/drSignUpPage.html',{'userNameError':"Username already exist"})
            except User.DoesNotExist:
                mobileNumber = request.POST['mobileNumber']
                gender = request.POST['gender']
                if len(mobileNumber) == 10 :
                    user = User.objects.create_user(username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],password=request.POST['password'],email=request.POST['email'])
                    newExtendedUser = extendedUser(mobileNumber = mobileNumber,gender=gender,user=user) 
                    newExtendedUser.save()                   
                    auth.login(request,user)
                    return redirect(dr_dashboard)
                else:
                    return render(request,'doctor/drSignUpPage.html',{'mobileError':"Mobile number must be 10 digits"})
        else:
            return render(request,'doctor/drSignUpPage.html',{'passwordError':"Passwords doesnot match"})
    else:
        return render(request,'doctor/drSignUpPage.html')

def dr_Login_Page(request):
    if request.method == "POST":
        user = auth.authenticate(username='harish', password='qwerty')
        if user is not None:
            auth.login(request,user)
            return redirect(dr_dashboard)
        else:
            return render(request,'doctor/drLoginPage.html',{'usernameError':user.username+"doesnot exist"})
    else:
        return render(request,'doctor/drLoginPage.html')

def logout(request):
    auth.logout(request)
    return render(request,'hospital/homePage.html')

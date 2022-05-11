import email
from django.urls import reverse
from django.shortcuts import render,redirect
from django.views.generic import FormView,View
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from accounts.models import User
# Create your views here.
class LoginView(View):


    def get(self,request,**kwargs):
        if request.user.is_authenticated:
            raise Http404

        return render(request,'account_login.html')


    def post(self,request,**kwargs):
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if not user:
            return render(request,'account_login.html',context={'login_fail':True})
        
        login(request,user)
        #If there is a next parameter in the link 
        try:
            next_url=request.GET['next']
        except:
            return redirect(reverse('post-list')) 

        else:
            return redirect(next_url)   #redirect to that parameter url



class SignUpView(View):
    

    def get(self,request,**kwargs):

        return render(request,'account_signup.html')


    def post(self,request,**kwargs):

        email=request.POST['email']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']

        if  (first_name.strip()) and (last_name.strip()):
            pass

        else:
            return render(request,'account_signup.html',context={'fail_msg':"Make sure your name inputs are filled"})


        if request.POST['password1'] == request.POST['password2']:
            password=request.POST['password1']

            user=User.objects.create_user(email=email,password=password,
            first_name=first_name,last_name=last_name
            )

            login(request,user)

            redirect(reverse('post-list'))

            

        else:
            return render(request,'account_signup.html',context={'fail_msg':"Make sure your passwords match."})






       



class LogoutView(View):



    def get(self,request,**kwargs):
    
        if request.user.is_authenticated:
            logout(request)
            return redirect(reverse('post-list'))
        else:
            raise Http404



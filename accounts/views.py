from django.urls import reverse
from django.shortcuts import render,redirect
from django.views.generic import FormView,View
from django.contrib.auth import login,authenticate
# Create your views here.
class LoginView(View):


    def get(self,request,**kwargs):

        return render(request,'account_login.html')


    def post(self,request,**kwargs):
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if not user:
            return render(request,'account_login.html',context={'login_fail':True})
        
        login(user)

        return redirect(reverse('post-list'))
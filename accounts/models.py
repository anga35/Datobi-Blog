import email
from re import T
import django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User,PermissionsMixin,BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,first_name,last_name,active=True,staff=False,admin=False,is_superuser=False):
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.first_name=first_name
        user.last_name=last_name
        user.is_active=active
        user.is_admin=admin
        user.is_staff=staff
        
        user.is_superuser=is_superuser
        user.save(using=self.db)
        return user

    def create_staff_user(self,email,password,first_name,last_name):
        user=self.create_user(email,password,first_name,last_name,staff=True)
        return user


    def create_superuser(self,email,password,first_name,last_name):
        user=self.create_user(email,password,first_name,last_name,staff=True,admin=True,is_superuser=True)
        return user



class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD='email'

    REQUIRED_FIELDS = ['first_name','last_name']

    objects=UserManager()


    def __str__(self) -> str:
        return self.email


    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'



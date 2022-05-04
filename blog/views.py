from webbrowser import get
from blog.models import Post
from pyexpat import model
from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView,ListView

# Create your views here.



class PostDetailView(DetailView):
    model=Post



class PostListView(ListView):
    
    model=Post
    

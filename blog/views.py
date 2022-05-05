from webbrowser import get
from blog.models import Post
from pyexpat import model
from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView,ListView
from blog.forms import PostForm


# Create your views here.

class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
    redirect_field_name='post_detail.html'


class PostDetailView(DetailView):
    model=Post



class PostListView(ListView):
    
    model=Post
    

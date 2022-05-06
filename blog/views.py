
from typing import Any
from webbrowser import get

from django.http import HttpRequest, HttpResponse
from blog.models import Post
from pyexpat import model
from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView,ListView,UpdateView
from blog.forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    form_class=PostForm
    login_url='/login/'
    redirect_field_name='post_detail.html'


class PostDetailView(DetailView):
    model=Post



class PostListView(ListView):
    
    model=Post
    
    def get_queryset(self):
        qs=super().get_queryset()
        qs=qs.filter(publish_date__isnull=False)
        return qs

class PostDraftsView(ListView):
    model=Post
    template_name='blog/post_drafts.html'




    def get_queryset(self):
        qs= Post.objects.filter(publish_date__isnull=True)
        print(qs)
        return qs


class PostUpdateView(UpdateView):
    model=Post
    form_class=PostForm
    


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.get_object().title='Buss'
        self.get_object().unpublish()
        print(self.get_object().publish_date)
        
        
        return super().get(request, *args, **kwargs)


    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.get_object().publish_date=None
        print(self.get_object().publish_date)
        self.get_object().save()
        return super().post(request, *args, **kwargs)


    


def publish(request,**kwargs):
    pk=kwargs['pk']

    post=Post.objects.get(pk=pk)
    post.publish()
    return redirect('post-list')


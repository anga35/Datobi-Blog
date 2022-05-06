
from webbrowser import get
from blog.models import Post
from pyexpat import model
from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView,ListView
from blog.forms import PostForm
from django.shortcuts import redirect

# Create your views here.

class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
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


def publish(request,**kwargs):
    pk=kwargs['pk']

    post=Post.objects.get(pk=pk)
    post.publish()
    return redirect('post-list')


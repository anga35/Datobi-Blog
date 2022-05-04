from django.urls import path
from blog.views import PostListView


urlpatterns=[
path('all/',PostListView.as_view(),name='post-list')


]
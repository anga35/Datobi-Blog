from django.urls import path
from blog.views import PostListView,PostDetailView


urlpatterns=[
path('all/',PostListView.as_view(),name='post-list'),
path('<int:pk>',PostDetailView.as_view(),name='post-detail')

]
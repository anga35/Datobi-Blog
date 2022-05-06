from django.urls import path
from blog.views import PostListView,PostDetailView,PostCreateView,PostDraftsView,publish


urlpatterns=[
path('all/',PostListView.as_view(),name='post-list'),
path('<int:pk>',PostDetailView.as_view(),name='post-detail'),
path('create/',PostCreateView.as_view(),name='post-create'),
path('drafts/',PostDraftsView.as_view(),name='post-drafts'),
path('publish/<int:pk>/',publish, name='post-publish')
]
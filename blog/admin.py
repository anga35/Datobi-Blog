from django.contrib import admin
from blog.models import Post
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(Post)
User = get_user_model()
admin.site.register(User)
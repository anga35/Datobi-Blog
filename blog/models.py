from distutils.command.upload import upload
from operator import mod
from turtle import title
from django.db import models
from psycopg2 import Timestamp
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120)
    content=RichTextField(blank=True,null=True)
    author=models.CharField(max_length=50)
    date_created=models.DateTimeField(auto_now_add=True)
    publish_date=models.DateTimeField(null=True,blank=True)
    image=models.ImageField(upload_to='post_thumbnail',null=True)


    def __str__(self) -> str:
        return self.title

    def unpublish(self):
        self.publish_date=None
        self.save()

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def get_absolute_url(self):
        
        return reverse('post-detail', kwargs={'pk': self.pk})

from operator import mod
from django.db import models
from psycopg2 import Timestamp
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    author=models.CharField(max_length=50)
    date_created=models.DateTimeField(auto_now_add=True)
    publish_date=models.DateTimeField(null=True,default=None)
    

    def publish(self):
        self.publish_date=timezone.now()
        self.save()



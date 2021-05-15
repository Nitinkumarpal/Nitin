from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    auther= models.CharField(max_length=200)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class Contact_Us(models.Model):

    name=models.CharField(max_length=150)
    
    email=models.CharField(max_length=150)
    comment=models.CharField(max_length=500)
    
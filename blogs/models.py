from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    '''
    Category Model related with posts
    :params:
    category with choices
    '''
    title = models.CharField(max_length=15)



class Blog(models.Model):
    '''
    Blog model
    :params:
    owner foreign key based on Usero of the blog
    '''
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(User)



class Post(models.Model):
    ''' 
    Post Model
    :params: 
    title of blog
    introduction_text not obligatory max_length
    body_text body content
    URL_media String url for image or video
    modified and created when blog was created and modified
    '''
    title = models.CharField(max_length=30)
    introduction_text = models.CharField(max_length=300, blank=True)
    body_text = models.TextField()
    URL_media = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    blog = models.ForeignKey(Blog)


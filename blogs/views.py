from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class BlogsView(View):
    '''
    Get all blogs
    :params: request
    :return: All blogs with name and identifier of user 
    in a templates (Username)
    '''

    def get(self, request):
        return HttpResponse('blogs view')


class PostsView(View):
    '''
    Get the post of a user
    :params: request, username
    :return: All post of a username blog and pk in a tempalte
    of every post
    '''

    def get(self, request, username):
        return HttpResponse('posts views')


class PostDetailView(View):
    '''
    Get detail of a post
    :params: request, pk
    :return: Detail of a post in a template
    '''

    def get(self, request, username, pk):
        return HttpResponse('Post detail')


class CreatePostView(View):
    '''
    Creation of Post
    :params: request PostData
    :return: OK or not OK saved data
    '''

    def get(self, request):
        return HttpResponse('Creation Post')

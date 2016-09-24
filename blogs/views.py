from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from blogs.models import Blog, Post
from django.contrib.auth.models import User


# Create your views here.

class BlogsView(View):

    def get(self, request):
        '''
        Get all blogs
        :params: request
        :return: All blogs with name and identifier of user 
        in a templates (Username)
        '''
        blogs = Blog.objects.all().order_by('?')
        context = {'blogs_list': blogs}
        return render(request, 'blogs/blogs-home.html', context)


class PostsView(View):
    '''
    Get the post of a user
    :params: request, username
    :return: All post of a username blog and pk in a tempalte
    of every post
    '''

    def get(self, request, username):
        # Context variables
        error = None
        posts = ''
        blog_username = ''

        # Actions
        owner = User.objects.filter(username=username)
        if len(owner) == 0:
            error = 'The user you look for doesn\'t match with our Database'
        else:
            blog = Blog.objects.filter(owner=owner).select_related('owner')
            if len(blog) == 0:
                error = 'The user hasn\'t got any blog yet'
            else:
                posts = Post.objects.select_related().filter(blog=blog)
                blog_username = username
                if len(posts) == 0:
                    error = 'The blog hasn\'t got any post yet'

        # Tempalte Context
        context = {
            'post_list': posts,
            'username': username,
            'error': error
        }
        return render(request, 'blogs/blog-posts.html', context)


class PostDetailView(View):
    '''
    Get detail of a post
    :params: request, pk
    :return: Detail of a post in a template
    '''

    def get(self, request, username, pk):
        # Context Variables
        post = ''
        error = None
        blog_username = ''

        # Actions
        owner = User.objects.filter(username=username)
        if len(owner) == 0:
            error = 'The user you look for doesn\'t match with our Database'
        else:
            blog = Blog.objects.filter(owner=owner).select_related('owner')
            if len(blog) == 0:
                error = 'The user hasn\'t got any blog yet'
            else:
                posts = Post.objects.select_related().filter(blog=blog, pk=pk)
                if len(posts) == 0:
                    error = 'These post does\'t not exists'
                else:
                    post = post[0]
                    blog_username = username

        # Template context
        context = {
            'post': post,
            'error': error
        }
        return render(request, 'blogs/post-detail.html', context)


class CreatePostView(View):
    '''
    Creation of Post
    :params: request PostData
    :return: OK or not OK saved data
    '''

    def get(self, request):
        return HttpResponse('Creation Post')

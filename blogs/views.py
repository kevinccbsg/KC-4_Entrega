from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User

from blogs.models import Blog, Post
from blogs.forms import PostForm


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

    def get(self, request):
        '''
        Post Form render. 
        If data are correct the form save the content if not sends a feedback.
        User must logged
        '''
        success_message = ''
        post = Post()
        post_form = PostForm()
        # Template context
        context = {
            'form': post_form,
            'message': success_message
        }
        return render(request, 'blogs/post-create.html', context)

    def post_creation(self, request):
        '''
        Post Form render. 
        If data are correct the form save the content if not sends a feedback.
        User must logged
        :param: request
        '''
        success_message = ''
        post_instance = PostForm()
        post_form = PostForm(request.POST, instance=post_instance)
        if post_form.is_valid():
            new_post = post_form.save()
            post_form = PostForm()
            success_message = 'Post succesfully created'
        context = {
            'form': post_form,
            'message': success_message
        }
        return render(request, 'blogs/post-create.html', context)

from django.forms import ModelForm
from blogs.models import Post


class PostForm(ModelForm):
    '''
    Form to create a Post
    '''
    class Meta:
        model = Post
        exclude = ('blog',)

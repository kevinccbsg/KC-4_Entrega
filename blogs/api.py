from blogs.models import Blog
from rest_framework.generics import ListCreateAPIView
from blogs.serializers import BlogSerializer
from rest_framework import filters
__author__ = 'kevinccbsg'


class BlogListAPI(ListCreateAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('title',)

from blogs.models import Blog
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from blogs.serializers import BlogSerializer
__author__ = 'kevinccbsg'


class BlogListAPI(ListCreateAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


#class UserDetailAPI(RetrieveUpdateDestroyAPIView):
#
#    queryset = User.objects.all()
#    serializer_class = BlogSerializer


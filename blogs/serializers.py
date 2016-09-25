from blogs.models import Blog
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

__author__ = 'kevinccbsg'


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
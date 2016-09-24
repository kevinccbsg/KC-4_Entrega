from django.conf.urls import url
from blogs.views import

urlpatterns = [
    url(r'^$', , name='blogs_list'),
    url(r'^(?P<username>[a-z]\w+)$', , name='posts_of_user_blog'),
    url(r'^(?P<username>[a-z]\w+)/(?P<pk>[0-9]+)$', , name='post_user_detail'),
]

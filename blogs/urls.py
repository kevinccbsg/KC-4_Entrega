from django.conf.urls import url
from blogs.views import BlogsView, PostsView, PostDetailView

urlpatterns = [
    url(r'^$', BlogsView.as_view(), name='blogs_list'),
    url(r'^(?P<username>[a-z]\w+)$',
        PostsView.as_view(), name='posts_of_user_blog'),
    url(r'^(?P<username>[a-z]\w+)/(?P<pk>[0-9]+)/$',
        PostDetailView.as_view(), name='post_user_detail'),
]

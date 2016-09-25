"""sharend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blogs import urls as blogs_url
from blogs.views import CreatePostView
from users import urls as users_url
from blogs.api import BlogListAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Blogs URL
    url(r'^blogs/', include(blogs_url)),
    # API Blog
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='blogs_api_view'),

    # url(r'^$', , name='creation_blog'),
    url(r'^createpost/$', CreatePostView.as_view(), name='creation_post'),

    # Users URL
    url(r'', include(users_url)),
]

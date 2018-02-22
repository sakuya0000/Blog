"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from Blog.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^regist/$', regist),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', get_blogs),
    url(r'^detail/(\d+)/$', get_details, name='blog_get_detail')
]

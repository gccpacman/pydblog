from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^/', include('blog.urls', namespace='blog')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^administrator/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
]

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^about/$', views.BlogAbout.as_view(), name='about'),
    url(r'^post/(?P<slug>[-\w]+)$', views.BlogDetail.as_view(), name='post'),
    url(r'^gallery/$', views.BlogGallery.as_view(), name='gallery'),
]

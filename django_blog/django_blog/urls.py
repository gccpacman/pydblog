from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

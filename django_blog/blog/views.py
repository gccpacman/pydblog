from django.views import generic
from blog import models


class BlogAbout(generic.DetailView):
    template_name = "blog/about.html"

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/index.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/post.html"
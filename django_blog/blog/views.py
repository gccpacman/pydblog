from django.views import generic
from blog import models


class BlogAbout(generic.TemplateView):
    template_name = "blog/about.html"

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/index.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/post.html"
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        #slug = kwargs.get('slug')
        #context['post'] = models.Entry.objects.get(slug=slug)
        #import ipdb; ipdb.set_trace()
        return context
    
class BlogGallery(generic.ListView):
    model = models.Entry
    template_name = "blog/gallery.html"
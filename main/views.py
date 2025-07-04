from django.views.generic.base import TemplateView
from .models import Hero,About,Project

# Create your views here.


class IndexPageView(TemplateView):
    template_name='index.html'


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['hero_data'] = Hero.objects.all()
        context['about_data']=About.objects.all()
        context['project_data']=Project.objects.all()
        return context
    
from django.views.generic import ListView
from ideas.models import Idea


class HomeView(ListView):
    model = Idea
    template_name = 'common/index.html'
    context_object_name = 'ideas'

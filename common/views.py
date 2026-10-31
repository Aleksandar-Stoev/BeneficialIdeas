from django.views.generic import TemplateView
from ideas.models import Idea


class HomeView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_ideas'] = Idea.objects.order_by('-created_at')[:3]
        context['top_ideas'] = Idea.objects.order_by('-inspiration_coins')[:3]
        context['total_ideas'] = Idea.objects.count()
        return context

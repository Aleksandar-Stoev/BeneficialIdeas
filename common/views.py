from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from common.forms import CommentForm
from ideas.models import Idea


class HomeView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_ideas'] = Idea.objects.order_by('-created_at')[:3]
        context['top_ideas'] = Idea.objects.order_by('-inspiration_coins')[:3]
        context['total_ideas'] = Idea.objects.count()
        return context


@login_required
def add_comment(request, pk):
  if request.method == 'POST':
    idea = get_object_or_404(Idea, pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.idea = idea
      comment.author = request.user
      comment.save()

    referer = request.META.get('HTTP_REFERER', 'home')
    return redirect(f'{referer}#idea-{pk}')

  return redirect('home')

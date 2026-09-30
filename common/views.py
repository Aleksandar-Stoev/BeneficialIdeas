from django.views.generic import ListView
from common.forms import SearchForm
from ideas.models import Idea


class HomeView(ListView):
    model = Idea
    template_name = 'common/index.html'
    context_object_name = 'ideas'

    def get_queryset(self):
        queryset = super().get_queryset()

        self.form = SearchForm(self.request.GET or None)

        if self.form.is_valid():
            query = self.form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

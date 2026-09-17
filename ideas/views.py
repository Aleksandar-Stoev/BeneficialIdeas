from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.db import transaction
from ideas.models import Idea
from ideas.forms import IdeaForm, SuppliesFormSet


class ProjectFormSetMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['formset'] = SuppliesFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = SuppliesFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                self.object = form.save()
                formset.instance = self.object
                formset.save()

            return super().form_valid(form)

        else:
            return self.form_invalid(form)


class IdeaCreateView(ProjectFormSetMixin, CreateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('idea-list')


class IdeaUpdateView(ProjectFormSetMixin, UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('idea-list')

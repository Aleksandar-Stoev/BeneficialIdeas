from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
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


class IdeaCreateView(LoginRequiredMixin, ProjectFormSetMixin, CreateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('idea-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IdeaUpdateView(LoginRequiredMixin, ProjectFormSetMixin, UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('idea-list')


class IdeaListView(ListView):
    model = Idea
    template_name = 'ideas/idea_list.html'
    context_object_name = 'ideas'
    paginate_by = 6


class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'ideas/idea_detail.html'
    context_object_name = 'idea'


@login_required
def support_idea_view(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    profile = request.user.profile

    if idea.author != request.user and idea not in profile.supported_ideas.all():
        if profile.inspiration_coins >= 10:
            with transaction.atomic():

                profile.inspiration_coins -= 10
                profile.save()

                idea.inspiration_coins += 10
                idea.save()

                profile.supported_ideas.add(idea)

    return redirect('idea-detail', pk=idea.pk)

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.db import transaction
from common.forms import SearchForm
from ideas.mixins import ProjectFormSetMixin
from ideas.models import Idea
from ideas.forms import IdeaForm


class IdeaCreateView(LoginRequiredMixin, ProjectFormSetMixin, CreateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('ideas:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IdeaUpdateView(LoginRequiredMixin, ProjectFormSetMixin, UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('ideas:list')


class IdeaListView(ListView):
    model = Idea
    template_name = 'ideas/idea_list.html'
    context_object_name = 'ideas'
    paginate_by = 5

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

                if idea.inspiration_coins >= 100 and idea.status == Idea.StatusChoices.PENDING:
                    idea.status = Idea.StatusChoices.APPROVED

                idea.save()

                profile.supported_ideas.add(idea)

    return redirect('ideas:detail', pk=idea.pk)


@staff_member_required
def approve_idea_view(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if idea.status == Idea.StatusChoices.PENDING:
        idea.status = Idea.StatusChoices.APPROVED
        idea.save()

    return redirect('ideas:detail', pk=idea.pk)

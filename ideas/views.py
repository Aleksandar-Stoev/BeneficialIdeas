from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from common.forms import SearchForm, CommentForm
from ideas.forms import IdeaCreateForm, IdeaUpdateForm, IdeaDeleteForm
from ideas.mixins import ProjectFormSetMixin
from ideas.models import Idea


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


class IdeaCreateView(LoginRequiredMixin, ProjectFormSetMixin, CreateView):
    model = Idea
    form_class = IdeaCreateForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('ideas:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IdeaUpdateView(LoginRequiredMixin, ProjectFormSetMixin, UpdateView):
    model = Idea
    form_class = IdeaUpdateForm
    template_name = 'ideas/manage_idea.html'
    success_url = reverse_lazy('ideas:list')


class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'ideas/idea_detail.html'
    context_object_name = 'idea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class IdeaDeleteView(LoginRequiredMixin, DeleteView):
    model = Idea
    form_class = IdeaDeleteForm
    template_name = 'ideas/idea_delete.html'
    success_url = reverse_lazy('ideas:list')


@login_required
def support_idea_view(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    profile = request.user.profile

    is_author = (idea.author == request.user)
    is_already_supported = idea in profile.supported_ideas.all()
    has_enough_coins = profile.inspiration_coins >= 10

    if not is_author and not is_already_supported and has_enough_coins:
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

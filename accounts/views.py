from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accounts.forms import CustomUserCreationForm, ProfileEditForm, ProfileDeleteForm
from accounts.models import Profile
from common.mixins import AuthorRequiredMixin

User = get_user_model()


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')


class ProfileDetailView(AuthorRequiredMixin, DetailView):
    model = Profile
    author_field = 'user'
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related('user')
            .prefetch_related('user__ideas', 'supported_ideas')
        )

class ProfileUpdateView(AuthorRequiredMixin, UpdateView):
    model = Profile
    author_field = 'user'
    form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'

    def get_success_url(self):
        return reverse('accounts:details', kwargs={'pk': self.object.user.pk})


class ProfileDeleteView(AuthorRequiredMixin, DeleteView):
    model = Profile
    author_field = 'user'
    form_class = ProfileDeleteForm
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        profile = self.get_object()
        user = profile.user

        user.delete()

        return HttpResponseRedirect(self.get_success_url())

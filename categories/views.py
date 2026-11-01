from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from categories.mixins import StaffRequiredMixin
from categories.models import Category


class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'slug', 'description']
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('categories:list')


class CategoryDeleteView(StaffRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('categories:list')

class CategoryListView(StaffRequiredMixin, ListView):
  model = Category
  template_name = 'categories/category_list.html'
  context_object_name = 'categories'

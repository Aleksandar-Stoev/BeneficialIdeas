from django.contrib import admin
from unfold.admin import ModelAdmin
from ideas.models import Idea


@admin.register(Idea)
class IdeaAdmin(ModelAdmin):
    list_display = ('title', 'description', 'display_categories')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('category')

    @admin.display(description='Categories')
    def display_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])

from django.contrib import admin
from ideas.models import Idea


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'display_categories')

    def display_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])

    display_categories.short_description = 'Categories'

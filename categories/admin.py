from django.contrib import admin
from unfold.admin import ModelAdmin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass

from django.contrib import admin
from unfold.admin import ModelAdmin
from supplies.models import Supplies


@admin.register(Supplies)
class SuppliesAdmin(ModelAdmin):
    pass

from django.contrib import admin
from supplies.models import Supplies


@admin.register(Supplies)
class SuppliesAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from unfold.admin import ModelAdmin
from accounts.models import BenevolentUser


@admin.register(BenevolentUser)
class BenevolentUserAdmin(ModelAdmin):
    pass
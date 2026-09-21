from django.contrib import admin
from accounts.models import BenevolentUser


@admin.register(BenevolentUser)
class BenevolentUserAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from django.contrib.auth import get_user_model
from unfold.admin import ModelAdmin

User = get_user_model()

@admin.register(User)
class BenevolentUserAdmin(ModelAdmin):
    pass

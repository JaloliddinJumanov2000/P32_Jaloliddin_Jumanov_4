from django.contrib import admin
from .models import Suggestion


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'user__username']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']
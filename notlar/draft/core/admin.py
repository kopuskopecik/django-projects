from django.contrib import admin
from core.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    ordering = ['title']
    actions = ['make_active']

    def make_active(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, "Selected entries are successfully marked as True")
    make_active.short_description = "Mark selected stories as True"

admin.site.register(Entry, EntryAdmin)

from crum import get_current_user
from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # Make the created field (which is auto_now_add=True) readable; because it
    # is managed by django, and it's not editable. Thus, django doesn't show it
    # by default.
    readonly_fields = ('created',)

    list_display = ['title', 'important', 'created', 'completed', 'author', ]

    list_filter = ['important', ]

    search_fields = ['title', 'memo']

    date_hierarchy = 'created'

    ordering = ['completed', '-important', ]

    def get_queryset(self, request):
        queryset = super(TodoAdmin, self).get_queryset(request)
        return queryset.filter(author=get_current_user())


# Register your models here.
admin.site.register(Todo, TodoAdmin)

from django.contrib import admin
from list_item.models import ListItem


class ListItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'priority', 'list']
    list_filter = ['created', 'name', 'is_done', 'list']
    search_fields = ['name', 'list']


admin.site.register(ListItem, ListItemAdmin)

from django.contrib import admin

from api.models import List, Task


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    """ Lists """
    list_display = ('name', 'user', 'create_date')
    list_display_links = ('name', )
    list_filter = ('create_date', )
    search_fields = ('name', 'user', 'create_date')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """ Tasks """
    list_display = ('name', 'list', 'details', 'parent', 'create_date')
    list_display_links = ('name',)
    list_filter = ('create_date', 'list')
    search_fields = ('name', 'list', 'create_date')


admin.site.site_title = "ToDo"
admin.site.site_header = "ToDo"

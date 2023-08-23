from django.contrib import admin

from .models import Tag

admin.site.empty_value_display = 'Не указано'


@admin.register(Tag, site=admin.site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    ordering = ('tag',)

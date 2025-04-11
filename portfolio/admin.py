from django.contrib import admin
from .models import Project, Category, Tag  # Import your models

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible')
    filter_horizontal = ('tags',)  # Allows manual selection of tags

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_main_key')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_main_key')
    search_fields = ('name',)

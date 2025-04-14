from django.contrib import admin, messages
from django.shortcuts import redirect
from .models import Project, Category, Tag
from admin_extra_buttons.api import ExtraButtonsMixin, button
from .views import update_projects  


@admin.register(Project)
class ProjectAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ('name', 'visible')
    search_fields = ('name',)
    filter_horizontal = ('tags',)

    @button(label="Update Projects", html_attrs={"style" : "background-color: #66B266; color: white;"})
    def update_projects(self, request):
        update_projects()  
        self.message_user(request, "Projects updated from GitHub", messages.SUCCESS)
        return redirect("admin:portfolio_project_changelist")  # Redirect to admin list view


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_main_key')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_main_key')
    search_fields = ('name',)

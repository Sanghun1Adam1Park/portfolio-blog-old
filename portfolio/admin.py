from django.contrib import admin, messages
from django.shortcuts import redirect
from .models import Project, Category, Tag
from admin_extra_buttons.api import ExtraButtonsMixin, button
from .views import load_projects  


@admin.register(Project)
class ProjectAdmin(ExtraButtonsMixin, admin.ModelAdmin):

    @button(label="Load Projects", html_attrs={"style" : "background-color: #66B266; color: white;"})
    def update_projects(self, request):
        load_projects()  
        self.message_user(request, "Projects updated from GitHub", messages.SUCCESS)
        return redirect("admin:portfolio_project_changelist")  # Redirect to admin list view


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    None 
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    None 

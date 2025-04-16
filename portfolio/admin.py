from django.contrib import admin, messages
from django.shortcuts import redirect
from .models import Project, Category, Tag
from admin_extra_buttons.api import ExtraButtonsMixin, button
from .views import load_projects  

@admin.register(Project)
class ProjectAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ["name", "updated", "url", "visible", "display_tags", ] # Dispaly on the panel 
    search_fields = ["name", ] # Search Bar
    filter_horizontal = ('tags',) # For assinging tags 
    
    def display_tags(self, obj): # To display tags 
        return ", ".join(tag.name for tag in obj.tags.all())
    display_tags.short_description = 'Tags'
    
    @button(label="Load Projects", html_attrs={"style" : "background-color: #66B266; color: white;"})
    def update_projects(self, request):
        load_projects()  
        self.message_user(request, "Projects updated from GitHub", messages.SUCCESS)
        return redirect("admin:portfolio_project_changelist")  # Redirect to admin list view

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ] 
    search_fields = ["name", ]
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "category", ]  
    search_fields = ["name", ]
    list_filter = ["category", ]

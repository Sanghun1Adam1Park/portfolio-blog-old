from django.shortcuts import render, redirect
from github import Github
from .models import Project, Tag

# Request handling functions (views)
def about(request):
    """_summary_
        Returns HTML for 'about' page.
        
    Args:
        request (_type_): django request from ./urls.py
    """
    return render(request, 'portfolio/about.html', {})

def projects(request):
    """_summary_
        Returns HTML for 'about' page.
        
    Args:
        request (_type_): django request from ./urls.py
    """
    projects = Project.objects.all() # Get all projects ojbects from the database used to display projects
    tags = Tag.objects.all() # Get all tags ojbects from the database used in filter button
    return render(request, 'portfolio/projects.html', {'projects' : projects, 'tags': tags})

def analytics(request):
    """_summary_
        Returns HTML for 'analytics' page.
        
    Args:
        request (_type_): django request from ./urls.py
    """
    return render(request, 'portfolio/analytics.html', {})                                         

def filter(request, tag):
    """_summary_
        Returns HTML for 'filtered' page.
        
    Args:
        request (_type_): django request from ./urls.py
        tag (str): name tag to filter projects by
    """
    if tag.lower() == "all" :
        return redirect('projects') # Redirect to all projects if tag is "all"
    try:
        tag = Tag.objects.get(name__iexact=tag) # Get the tag object from DB
        if tag.is_category_tag:
            # Get all tags in the same category (excluding the category tag itself if needed)
            related_tags = Tag.objects.filter(category=tag.category)
            # Get projects that have ANY of the related tags
            projects = Project.objects.filter(tags__in=related_tags).distinct()
        else:
            projects = Project.objects.filter(tags=tag) # Get all projects that has the tag from DB
        tags = Tag.objects.all() # Get all tags from DB for filter button 
        return render(request, 'portfolio/filtered.html', {'projects' : projects, 'tag' : tag, 'tags': tags})
    except Tag.DoesNotExist:
        return redirect('projects') # Redirect to all projects if tag is not found

# DB managing functions (views)
def load_projects():
    """_summary_
        Updates the projects in the database by fetching from GitHub using GitHub REST API.   
    """
    hub = Github()
    
    my_repos = hub.get_user("sanghun1adam1park").get_repos()
    for repo in my_repos:
        Project.objects.update_or_create(
            id=repo.id, # Check if repo is already in, if in update else create 
            defaults={
                "name": repo.name,
                "description": repo.description or "no description",
                "url": repo.html_url,
                "updated": repo.updated_at,
            }
        )   

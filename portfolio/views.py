from django.shortcuts import render, redirect
from github import Github
from .models import Project, Tag

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
    projects = Project.objects.all() # Get all projects from the database
    tags = Tag.objects.all() # Get all tags from the database
    return render(request, 'portfolio/projects.html', {'projects' : projects, 'tags': tags})

def analytics(request):
    """_summary_
        Returns HTML for 'analytics' page.
        
    Args:
        request (_type_): django request from ./urls.py
    """
    return render(request, 'portfolio/analytics.html', {})

def load_projects():
    """_summary_
        Updates the projects in the database by fetching from GitHub using GitHub REST API.   
    """
    hub = Github()
    
    my_repos = hub.get_user("sanghun1adam1park").get_repos()
    for repo in my_repos:
        Project.objects.update_or_create(
            id=repo.id,
            defaults={
                "name": repo.name,
                "description": repo.description or "no description",
                "url": repo.html_url,
                "updated": repo.updated_at,
            }
        )                                            

def filter(request, tag):
    """_summary_
        Returns HTML for 'filtered' page.
        
    Args:
        request (_type_): django request from ./urls.py
        tag (_type_): tag to filter projects by
    """
    if tag.lower() == "all" :
        return redirect('projects') # Redirect to all projects if tag is "all"
    try:
        tag = Tag.objects.get(name__iexact=tag) # Get the tag object from the database
        projects = Project.objects.filter(tags__name__iexact=tag.name) # Get all projects from the database
        print(projects)       
        tags = Tag.objects.all() # Get all tags from the database
        return render(request, 'portfolio/filtered.html', {'projects' : projects, 'tag' : tag, 'tags': tags})
    except Tag.DoesNotExist:
        return redirect('projects') # Redirect to all projects if tag is not found

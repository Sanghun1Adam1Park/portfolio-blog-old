from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    """_summary_
        Returns HTML for 'about' page.
        
    Args:
        request (_type_): django request from ./urls.py
    """
    return render(request, 'portfolio/about.html', {})

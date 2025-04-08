from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('update/', views.update_projects, name='update'),
]

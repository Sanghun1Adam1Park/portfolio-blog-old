from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/filter-<str:tag>/', views.filter, name='filter'),
]

from django.db import models
from .fields import CaseInsensitiveCharField

class Project(models.Model):
    """_summary_
        Project model for storing project information.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    updated = models.DateTimeField(auto_now=False)
    visible = models.BooleanField(default=False) 
    tags = models.ManyToManyField('Tag', blank=True) 
    
    def __str__(self):
        return f"{self.name} - {self.description}"

class Category(models.Model):
    """Category model for grouping tags."""
    category_name = CaseInsensitiveCharField(max_length=255, unique=True, primary_key=True)
    color = models.CharField(max_length=7, default="#FFFFFF")  
    
    def __str__(self):
        return f'#{self.category_name}'

class Tag(Category):
    """Tag model associated with a category."""
    tag_name = CaseInsensitiveCharField(max_length=255, unique=True, primary_key=True)

    def __str__(self):
        return f'# {super.__str__} - {self.tag_name}'

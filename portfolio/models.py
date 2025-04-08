from django.db import models

# Create your models here.
class Project(models.Model):
    """_summary_
        Project model for storing project information.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    updated = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return f"{self.name} - {self.description}"

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ValidationError

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
    tags = models.ManyToManyField('Tag', blank=True)  # Many-to-many relationship with Tag
    
    def __str__(self):
        return f"{self.name} - {self.description}"

class Category(models.Model):
    """Category model for grouping tags."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    has_main_key = models.BooleanField(default=False)  # To identify main category
    color = models.CharField(max_length=7, default="#FFFFFF")  # Default color for the category
    visible = models.BooleanField(default=False)  # To identify main category
    
    def __str__(self):
        return f'#{self.name}'

class Tag(models.Model):
    """Tag model associated with a category."""
    name = models.CharField(max_length=255, unique=True)  # globally unique
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='main_tag')
    is_main_key = models.BooleanField(default=False)  # To identify main tag
    color = models.CharField(max_length=7, blank=True)  # Inherit color from category

    def save(self, *args, **kwargs):
        # Inherit color from the associated category
        if not self.color and self.category:
            self.color = self.category.color
        super().save(*args, **kwargs)
    
    def clean(self):
        # Check if another main tag already exists for the category
        if self.is_main_key:
            existing_main_tag = Tag.objects.filter(category=self.category, is_main_key=True).exclude(id=self.id).first()
            if existing_main_tag:
                raise ValidationError(f"A main tag already exists for the category '{self.category.name}'.")
    
    def __str__(self):
        return f'#{self.name}'

@receiver(post_save, sender=Category)
def create_default_tag(sender, instance, created, **kwargs):
    """_summary_
        Signal to create a default tag when a new category is created.
        Also sets the category as having a main key.
        """
    if created:
        Tag.objects.create(name=instance.name, category=instance, is_main_key=True)
        instance.has_main_key = True
        instance.save()

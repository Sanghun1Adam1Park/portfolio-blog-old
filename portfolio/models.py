from django.db import models

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
    
    class Meta:
        ordering = ["updated"]

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=7, blank=False)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """_summary_
            Creates category tag when you create new category.
        """
        created = not self.pk  # Check if this is a new instance
        super().save(*args, **kwargs) 
        if created:
            Tag.objects.create(
                name=f"{self.name}",
                category=self,
                is_category_tag=True
            )
    
    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='case_insensitive_name',
                violation_error_message="Name must be unique (case insensitive)"
            )
        ]

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tags')
    is_category_tag = models.BooleanField(default=False)  # Marks the tag that represents the whole category
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"
    
    class Meta:
        unique_together = [('name', 'category'), ('category', 'is_category_tag')]
        ordering = ['name']

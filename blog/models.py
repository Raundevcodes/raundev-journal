from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True) 
    
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  # views field added

    def __str__(self):
        return self.title

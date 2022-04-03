from importlib.metadata import requires

from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

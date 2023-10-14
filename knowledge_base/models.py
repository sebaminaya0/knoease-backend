from django.db import models
from authentication.models import User

class Document(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Section(models.Model):
    document = models.ForeignKey(Document, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Integration(models.Model):
    INTEGRATION_CHOICES = [
        ('zoom', 'Zoom'),
        ('gdrive', 'Google Drive'),
        # ... other integration types
    ]
    type = models.CharField(max_length=20, choices=INTEGRATION_CHOICES)
    document = models.ForeignKey(Document, related_name='integrations', on_delete=models.CASCADE)
    data = models.JSONField()  # Store integration data as JSON
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# Create your models here.

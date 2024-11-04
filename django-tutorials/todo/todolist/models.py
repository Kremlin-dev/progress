from django.db import models
from django.contrib.auth.models import User

class todolist(models.Model):
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Shopping', 'Shopping'),
    ]
    
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User,  null=True, on_delete=models.SET_NULL)
    deadline = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.title



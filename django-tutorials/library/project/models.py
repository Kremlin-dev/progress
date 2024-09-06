from django.db import models


class book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True)
    published_date = models.DateField(null=True)

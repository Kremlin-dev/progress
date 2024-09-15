from django.db import models

class register(models.Model):
    firstName = models.CharField(max_length=255, null = True)
    lastName = models.CharField(max_length = 255, null = True)
    email = models.EmailField(max_length=255, null = True)
    telephone = models.CharField(max_length=10, null=True)


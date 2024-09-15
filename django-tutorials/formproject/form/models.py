from django.db import models

class register(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length = 25)
    email = models.EmailField(max_length=255, unique=True)
    telephone = models.CharField(max_length=10, unique=True)


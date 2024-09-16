from django.db import models

class register(models.Model):
    firstName = models.CharField(max_length=255, null = True)
    lastName = models.CharField(max_length = 255, null = True)
    email = models.EmailField(max_length=255, null = True)
    telephone = models.CharField(max_length=10, null=True)

class hostel(models.Model):
    hostelName = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    manager= models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    rooms = models.IntegerField()


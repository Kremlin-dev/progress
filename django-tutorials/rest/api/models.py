from django.db import models

class userinfo(models.Model):
    username = models.CharField(max_length = 255, null = True)
    email = models.EmailField(max_length = 255, null = True)
    age = models.IntegerField(null = True)

# Create your models here.

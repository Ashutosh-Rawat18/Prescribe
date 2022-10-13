import email
from django.db import models

# Create your models here.


class patregtable(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    email = models.CharField(max_length=50)
    phoneno = models.IntegerField(max_length=10)
    address = models.CharField(max_length=500)
    password = models.CharField(max_length=50)

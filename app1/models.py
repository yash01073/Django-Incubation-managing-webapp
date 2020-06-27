from django.db import models

# Create your models here.
class AddUser(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    username = models.CharField(max_length=40,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=10)

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=200, blank=True, null=True)
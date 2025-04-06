from django.db import models
from user.models import User



class Teacher(models.Model):
    name = models.CharField(max_length=32)
    national_ID = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    email_address = models.EmailField(null=True, blank=True)
    profile = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"



class Student(models.Model):
    name = models.CharField(max_length=32)
    national_ID = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    email_address = models.EmailField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
       
    


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"




class Course(models.Model):
    name = models.CharField(max_length=32)
    teachers = models.ManyToManyField(Teacher, related_name= 'teacher')
    students = models.ManyToManyField(Student, related_name= 'student')
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    duration = models.TimeField(null=True, blank= True)
    price = models.BigIntegerField()
    Categories = models.ManyToManyField(Category, related_name= 'Categories')

    def __str__(self):
        return f"{self.name}"


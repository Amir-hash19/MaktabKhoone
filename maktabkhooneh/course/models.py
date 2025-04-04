from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    national_ID = models.IntegerField(unique= True)
    phone_number = models.CharField(max_length= 11, unique= True)
    emai_address = models.EmailField(null =True, blank=True)

    def __str__(self):
        return super().__str__()


class Student(models.Model):
    name = models.CharField(max_length=32)
    national_ID = models.IntegerField(unique= True)
    phone_number = models.CharField(max_length= 11, unique= True)
    emai_address = models.EmailField(null =True, blank=True)
    
    def __str__(self):
        return super().__str__()
    
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return super().__str__()

class Course(models.Model):
    name = models.CharField(max_length=32)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name= 'teacher')
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name= 'student')
    is_active = models.BooleanField()
    duration = models.TimeField(null=True, blank= True)
    price = models.BigIntegerField()
    Categories = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= 'Categories', null= True, blank= True)

    def __str__(self):
        return super().__str__()


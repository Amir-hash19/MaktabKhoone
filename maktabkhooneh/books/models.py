from django.db import models
from user.models import User
from django.utils import timezone
import random



class CategoryArticle(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f"{self.name}"




class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(to=CategoryArticle, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"




class CategoryBook(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f"{self.name}"
    



class Book(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="authorbook")
    category = models.ForeignKey(to=CategoryBook, on_delete=models.CASCADE,related_name="bookcategory")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(null=False, blank=False)



    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]
        ordering = ['-date_created']
        get_latest_by = "date_created"    

   
    
    def __str__(self):
        return "{} - {}".format(self.title, self.author)


        

class OTP(models.Model):
    phone = models.CharField(max_length=15)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


    def is_valid(self):
        return timezone.now() - self.created_at < timezone.timedelta(minutes=2)
    
    @staticmethod
    def generate_code():
        return str(random.randint(100000, 999999))

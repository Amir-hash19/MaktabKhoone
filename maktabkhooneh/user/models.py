from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, email, user_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        else:
            email = self.normalize_email(email)
            user = self.model(email=email, user_name=user_name)
            user.set_password(password)
            user.save()
            return user
        

    def create_superuser(self, email, user_name, password):
        user = self.create_user(email=email, user_name=user_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    


class User(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True)
    user_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13, null=True, blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)




    class Meta:
        indexes = [
            models.Index(fields=["user_name"])
        ] 
        
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    

    def __str__(self):
        return self.user_name

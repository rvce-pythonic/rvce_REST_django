from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_f):
        """Creates and saves user"""
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(email=self.normalize_email(email), **extra_f)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_super_user(self, email, password):
        """creates a super user"""
        user=self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)

        return user

class User(AbstractBaseUser,PermissionsMixin):
    """custom model that supports the email instead of name"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)

    objects=UserManager()

    USERNAME_FIELD='email'

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Profile(models.Model):
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='account/users', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

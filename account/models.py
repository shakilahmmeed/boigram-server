from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Profile(models.Model):
    bio = models.TextField(null=True)
    address = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    avatar = models.ImageField(upload_to='account/users', null=True)
    phone = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def _str__(self):
        return self.user.username

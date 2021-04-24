from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from account.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(upload_to='core/books')

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[
                                 MaxValueValidator(5), MinValueValidator(0)])

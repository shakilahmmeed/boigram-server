from django.contrib import admin
from core.models import Book, Author, Category

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)

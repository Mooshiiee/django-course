from django.contrib import admin

# Register your models here.

# import models from the same directory
from .models import Author, Book

# register the models to the admin site
admin.site.register(Author)
admin.site.register(Book)
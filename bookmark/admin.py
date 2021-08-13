from django.contrib import admin
from .models import Bookmark, Book_Category
# Register your models here.

admin.site.register(Bookmark)
admin.site.register(Book_Category)
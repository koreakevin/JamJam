from django import forms
from .models import Book_Category

class Book_CategoryForm(forms.ModelForm):
    class Meta:
        model = Book_Category
        fields = ['name']

class BookmarkAdmin(forms.ModelForm):
    list_display = ['id', 'book_site_name', 'book_url']
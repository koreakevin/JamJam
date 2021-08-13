from django.db import models
from django.urls import reverse_lazy

class Bookmark(models.Model) :
    book_site_name = models.CharField(max_length=50)
    book_url = models.URLField()
    book_category = models.ManyToManyField('book_category', blank=True)

    def __str__(self) :
        return self.book_site_name + " : " + self.book_url

    def get_absolute_url(self):
        return reverse_lazy('bookmark_detail', args = [self.id])

    class Meta :
        ordering = ['book_site_name']

#북마크 카테고리
class Book_Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
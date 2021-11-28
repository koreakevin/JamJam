from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from .models import Bookmark, Book_Category
from .forms import Book_CategoryForm


def bookmark_category(request, book_category=None):
    books = Bookmark.objects
    book_categorys = Book_Category.objects
    if request.method == 'POST':
        form = Book_CategoryForm(request.POST, instance=book_category)
        if form.is_valid():
            book_category = form.save(commit=False)
            if Book_Category.objects.filter(name=form.cleaned_data['name']):
                form = Book_CategoryForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'bookmark/bookmark_category.html', {'form': form, "error_message": error_message})
            else:
                book_category.name = form.cleaned_data['name']
                book_category.save()
            return redirect('bookmark_category')
    else:
        form = Book_CategoryForm(instance=book_category)
        return render(request, 'bookmark/bookmark_category.html', {'books': books, 'book_categorys': book_categorys, 'form': form})


def bookmark_list(request, book_category_id):
    book_category = get_object_or_404(Book_Category, id=book_category_id)
    return render(request, 'bookmark/bookmark_list.html', {'book_category': book_category})


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['book_site_name', 'book_url', 'book_category']
    template_name = 'bookmark/bookmark_update.html'


class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name = 'bookmark/bookmark_delete.html'
    success_url = '/'


class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['book_site_name', 'book_url', 'book_category']
    template_name = 'bookmark/bookmark_create.html'


class BookmarkDetail(DetailView):
    model = Bookmark
    template_name = 'bookmark/bookmark_detail.html'

# 북마크 메인


def bookmark_category(request):
    return render(request, 'bookmark_category.html')

# url 추가


def bookmark_create(request):
    return render(request, 'bookmark_create.html')

# 북마크 리스트 수정


def bookmark_update(request):
    return render(request, 'bookmark_update.html')

# 북마크 리스트


def bookmark_list(request):
    return render(request, 'bookmark_list.html')

# 북마크 추가 확인


def bookmark_detail(request):
    return render(request, 'bookmark_detail.html')

# 북마크 삭제 확인


def bookmark_delete(request):
    return render(request, 'bookmark_delete.html')

from django.shortcuts import render
from django.views import generic

from .models import Book


class NeededBooksListView(generic.ListView):
    model = Book
    template_name = 'books/needed_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all().filter(need_or_add=Book.NEED_OR_ADD_CHOICES[0][0], is_active=True).order_by('-date_created')


class AddedBooksListView(generic.ListView):
    model = Book
    template_name = 'books/added_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all().filter(need_or_add=Book.NEED_OR_ADD_CHOICES[1][0], is_active=True).order_by('-date_created')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

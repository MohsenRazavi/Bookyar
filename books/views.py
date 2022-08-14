from django.shortcuts import render

from django.http import HttpResponse


def needed_books(request):
    return render(request, 'books/needed_books.html')


def added_books(request):
    return render(request, 'books/added_books.html')


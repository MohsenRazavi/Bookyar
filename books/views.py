from django.shortcuts import render

from django.http import HttpResponse


def needed_books(request):
    return HttpResponse('needed books')


def added_books(request):
    return HttpResponse('added books')


from django.shortcuts import render
from django.http import HttpResponse


def blog_list(request):
    return HttpResponse('blog list')

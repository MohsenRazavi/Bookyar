from django.shortcuts import render
from django.views import generic

from .models import Post


class BlogList(generic.ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


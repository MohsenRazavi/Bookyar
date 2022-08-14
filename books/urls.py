from django.urls import path

from . import views

urlpatterns = [
    path('needed_books/', views.needed_books, name='needed_books'),
    path('added_books/', views.added_books, name='added_books'),
]
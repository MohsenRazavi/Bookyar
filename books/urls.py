from django.urls import path

from . import views

urlpatterns = [
    path('needed_books/', views.NeededBooksListView.as_view(), name='needed_books'),
    path('added_books/', views.AddedBooksListView.as_view(), name='added_books'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
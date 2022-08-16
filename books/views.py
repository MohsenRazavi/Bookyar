from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Book
from .forms import BookUpdateForm, BookCreateForm


class NeededBooksListView(generic.ListView):
    model = Book
    template_name = 'books/needed_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all().filter(need_or_add=Book.NEED_OR_ADD_CHOICES[0][0], is_active=True).order_by(
            '-date_created')


class AddedBooksListView(generic.ListView):
    model = Book
    template_name = 'books/added_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all().filter(need_or_add=Book.NEED_OR_ADD_CHOICES[1][0], is_active=True).order_by(
            '-date_created')


class BookDetailView(generic.DetailView, UserPassesTestMixin):
    model = Book
    template_name = 'books/book_detail.html'

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return obj.user == self.request.user


@login_required
def book_create_view(request):
    if request.method == "POST":
        create_form = BookCreateForm(request.POST, request.FILES)
        if create_form.is_valid():
            new_book = create_form.save(commit=False)
            new_book.user = request.user
            new_book.is_active = False
            new_book.save()
            create_form = BookCreateForm()
    else:
        create_form = BookCreateForm()
    return render(request, 'books/book_create_view.html', {
        'form': create_form,
    })


class BookUpdateView(generic.UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Book
    template_name = 'books/book_update_view.html'
    success_url = reverse_lazy('home')
    form_class = BookUpdateForm

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return obj.user == self.request.user


class BookDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Book
    template_name = 'books/book_delete_view.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return obj.user == self.request.user

from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreateForm, CustomUserUpdateForm
from books.models import Book


class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = get_user_model()
    form_class = CustomUserUpdateForm
    template_name = 'accounts/user_panel_information.html'

    def test_func(self):
        user = get_user_model().objects.get(pk=self.request.user.id)
        if user.is_superuser:
            return True
        else:
            return user.id == self.kwargs['pk']


@login_required
def user_needed_books_view(request, pk):
    user = request.user
    user_needed_books = user.books.all().filter(need_or_add='need').order_by('-time_created')
    return render(request, 'accounts/user_panel_neededbooks.html', {
        'user': user,
        'books': user_needed_books,
    })


@login_required
def user_added_books_view(request, pk):
    user = request.user
    user_added_books = user.books.all().filter(need_or_add='add').order_by('-time_created')
    return render(request, 'accounts/user_panel_addedbooks.html', {
        'user': user,
        'books': user_added_books,
    })


@login_required
def user_posts_view(request, pk):
    user = request.user
    user_posts = user.posts.all().order_by('-datetime_lastedit')
    return render(request, 'accounts/user_panel_posts.html', {
        'user': user,
        'posts': user_posts,
    })


@login_required
def user_out_view(request, pk):
    custom_user = get_user_model().objects.get(pk=pk)
    return render(request, 'accounts/user_out_view.html', {
        'custom_user': custom_user,
    })

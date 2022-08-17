from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreateForm, CustomUserUpdateForm


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

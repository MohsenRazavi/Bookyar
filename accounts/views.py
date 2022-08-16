from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import CustomUserCreateForm


class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

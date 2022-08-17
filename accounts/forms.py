from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'profile',
            'gender',
            'first_name',
            'last_name',
            'age',
            'biography'
        ]


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'profile',
            'gender',
            'age',
            'biography',
        ]

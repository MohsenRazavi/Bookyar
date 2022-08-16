from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
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
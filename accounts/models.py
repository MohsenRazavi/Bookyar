from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'femail'),
    )
    age = models.IntegerField(blank=True, null=True)
    profile = models.ImageField(upload_to='profiles/', blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)

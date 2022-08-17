from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'femail'),
    )
    age = models.IntegerField(blank=True, null=True)
    profile = models.ImageField(upload_to='profiles/', blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    biography = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('panel', args=[self.id])

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', _('male')),
        ('female', _('femail')),
    )
    age = models.IntegerField(blank=True, null=True, verbose_name=_('age'))
    profile = models.ImageField(upload_to='profiles/', blank=True, verbose_name=_('profile'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, verbose_name=_('gender'))
    biography = models.TextField(blank=True, verbose_name=_('biography'))
    phone = models.CharField(max_length=12, blank=True, verbose_name=_('phone'))
    address = models.TextField(blank=True, verbose_name=_('address'))

    def get_absolute_url(self):
        return reverse('panel', args=[self.id])

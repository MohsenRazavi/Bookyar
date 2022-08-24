from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _


class Book(models.Model):
    NEED_OR_ADD_CHOICES = (
        ('need', _('needed')),
        ('add', _('added')),
    )
    MAJOR_CHOICES = (
        ('riazi', _('riazi')),
        ('tajrobi', _('tajrobi')),
        ('ensani', _('ensani')),
        ('general', _('general')),
        ('other', _('other')),
    )

    GRADE_CHOICES = (
        ('ten', _('tenth')),
        ('ele', _('eleventh')),
        ('twe', _('twelfth')),
        ('alg', _('all grades')),
        ('oth', _('other')),

    )
    LESSON_CHOICES = (
        ('calculus', _('calculus')),
        ('physics', _('physics')),
        ('chemistry', _('chemistry')),
        ('geometry', _('geometry')),
        ('statistics and probability', _('statistics and probability')),
        ('discrete math', _('discrete math')),
        ('biology', _('biology')),
        ('persian', _('persian')),
        ('arabic', _('arabic')),
        ('english', _('english')),
        ('religion and life', _('religion and life')),
        ('other', _('other')),
    )

    title = models.CharField(max_length=200, blank=False, verbose_name=_('title'))
    book_official_link = models.TextField(blank=False, verbose_name=_('book official link'))
    publisher = models.CharField(max_length=100, blank=False, verbose_name=_('publisher'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    major = models.CharField(max_length=10, choices=MAJOR_CHOICES, blank=False, verbose_name=_('major'))
    grade = models.CharField(max_length=3, choices=GRADE_CHOICES, blank=False, verbose_name=_('grade'))
    lesson = models.CharField(max_length=30, choices=LESSON_CHOICES, blank=False, verbose_name=_('lesson'))
    need_or_add = models.CharField(max_length=5, choices=NEED_OR_ADD_CHOICES, blank=False, verbose_name=_('need or add'))
    year = models.IntegerField(verbose_name=_('publish year'))
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), related_name='books', on_delete=models.CASCADE)
    is_active = models.BooleanField()
    book_cover = models.ImageField(upload_to='book_covers/', blank=True, verbose_name=_('book cover'))

    def __str__(self):
        return f"{self.title} , {self.grade}"

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])

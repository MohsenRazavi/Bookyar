from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    NEED_OR_HAVE_CHOICES = (
        ('need', 'needed'),
        ('add', 'added'),
    )

    GRADE_CHOICES = (
        ('ten', 'tenth'),
        ('ele', 'eleventh'),
        ('twe', 'twelfth'),
        ('alg', 'all grades'),
        ('oth', 'other'),

    )
    LESSON_CHOICES = (
        ('calculus', 'calculus'),
        ('physics', 'physics'),
        ('chemistry', 'chemistry'),
        ('geometry', 'geometry'),
        ('statistics and probability', 'statistics and probability'),
        ('discrete math', 'discrete math'),
        ('biology', 'biology'),
        ('persian', 'persian'),
        ('arabic', 'arabic'),
        ('english', 'english'),
        ('religion and life', 'religion and life'),
        ('other', 'other'),
    )

    title = models.CharField(max_length=200, blank=False)
    book_official_link = models.TextField(blank=False)
    grade = models.CharField(max_length=3, choices=GRADE_CHOICES, blank=False)
    lesson = models.CharField(max_length=30, choices=LESSON_CHOICES, blank=False)
    need_or_add = models.CharField(max_length=5, choices=NEED_OR_HAVE_CHOICES, blank=False)
    year = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField()
    book_cover = models.ImageField(upload_to='book_covers/', blank=True)

    def __str__(self):
        return f"{self.title} , {self.grade}"


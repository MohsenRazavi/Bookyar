from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
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
    year = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)





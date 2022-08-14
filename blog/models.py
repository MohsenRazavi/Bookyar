from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
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

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    publisher = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    lesson = models.CharField(max_length=30, choices=LESSON_CHOICES, blank=False, default=LESSON_CHOICES[-1])
    grade = models.CharField(max_length=3, choices=GRADE_CHOICES, blank=False, default=GRADE_CHOICES[-1])
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_lastedit = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    post_cover = models.ImageField(upload_to='post_covers/', blank=True)

    def __str__(self):
        return f"{self.title} | {self.publisher}"

    # def get_absolute_url(self):


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} : {self.text} | {self.post}"

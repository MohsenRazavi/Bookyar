from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _


class Post(models.Model):
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

    author = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, verbose_name=_('title'))
    publisher = models.CharField(max_length=200, blank=False, verbose_name=_('publisher'))
    description = models.TextField(verbose_name=_('description'))
    lesson = models.CharField(max_length=30, choices=LESSON_CHOICES, blank=False, default=LESSON_CHOICES[-1],
                              verbose_name=_('lesson'))
    grade = models.CharField(max_length=3, choices=GRADE_CHOICES, blank=False, default=GRADE_CHOICES[-1],
                             verbose_name=_('grade'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_lastedit = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    post_cover = models.ImageField(upload_to='post_covers/', blank=True, verbose_name=_('post_cover'))
    link = models.TextField(blank=False, verbose_name=_('official_link'))

    def __str__(self):
        return f"{self.title} | {self.publisher} | {self.author}"

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_('text'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    recommend = models.BooleanField(default=True, verbose_name=_('recommend'))

    def __str__(self):
        return f"{self.user} : {self.text} | {self.post}"

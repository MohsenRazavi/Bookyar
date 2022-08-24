from django import forms
from django.utils.translation import gettext as _

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
            'recommend',
        ]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'publisher',
            'lesson',
            'grade',
            'post_cover',
            'link',
            'description',
        ]


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'publisher',
            'lesson',
            'grade',
            'post_cover',
            'description',
        )

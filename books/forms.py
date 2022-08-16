from django import forms

from .models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'publisher',
            'lesson',
            'grade',
            'book_cover',
            'major',
            'need_or_add',
            'year',
            'book_official_link',
            'description',
        )


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'publisher',
            'lesson',
            'grade',
            'book_cover',
            'major',
            'need_or_add',
            'year',
            'book_official_link',
            'description',
        )

from modeltranslation.translator import TranslationOptions, translator

from .models import Book


class BookTranslation(TranslationOptions):
    fields = (
        'major',
        'grade',
        'lesson',
    )


translator.register(Book, BookTranslation)

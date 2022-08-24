from modeltranslation.translator import translator, TranslationOptions

from .models import Post


class PostTranslation(TranslationOptions):
    fields = (
        'title',
        'publisher',
        'lesson',
        'grade',
    )


translator.register(Post, PostTranslation)

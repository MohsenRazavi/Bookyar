from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'major',
        'grade',
        'lesson',
        'date_created',
        'is_active',
        'need_or_add',
    )

    list_editable = (
        'is_active',
    )
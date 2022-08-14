from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'grade',
        'lesson',
        'datetime_lastedit',
        'is_active'
    )

    list_editable = (
        'is_active',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
        'text',
        'recommend',
        'datetime_created',
        'is_active',
    )

    list_editable = ('is_active',)
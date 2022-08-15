from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy

from .models import Post, Comment
from .forms import CommentForm


class BlogPostList(generic.ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().filter(is_active=True).order_by('-datetime_lastedit')


def blog_post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment.all().filter(is_active=True).order_by('-datetime_created')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


class BlogPostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = (
        'title',
        'publisher',
        'lesson',
        'grade',
        'post_cover',
        'description',
        'author'
    )

    template_name = 'blog/blog_add_post.html'


class BlogPostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = (
        'title',
        'publisher',
        'lesson',
        'grade',
        'post_cover',
        'description',

    )
    template_name = 'blog/blog_update_post.html'

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return obj.user == self.request.user


class BlogPostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/blog_delete_post.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return obj.user == self.request.user


class BlogCommentDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = 'blog/blog_comment_delete.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return obj.user == self.request.user

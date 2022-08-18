from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post
from .models import Comment


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='test-user'
        )
        cls.new_post_active = Post.objects.create(
            title='test_title',
            author=cls.user,
            publisher='test',
            lesson='persian',
            grade='other',
            is_active=True,
        )
        cls.new_post = Post.objects.create(
            title='test_title_',
            author=cls.user,
            publisher='test',
            lesson='persian',
            grade='other',
            is_active=False,
        )
        cls.comment_active = Comment.objects.create(
            user=cls.user,
            post=cls.new_post_active,
            text='test comment active',
            is_active=True
        )

        cls.comment = Comment.objects.create(
            user=cls.user,
            post=cls.new_post_active,
            text='test comment',
            is_active=False
        )

    def test_urls_and_names(self):
        response1 = self.client.get(reverse('blog_list'))
        self.assertEqual(response1.status_code, 200)

        response2 = self.client.get(reverse('blog_detail', args=[self.new_post_active.id]))
        self.assertEqual(response2.status_code, 200)

    def test_blog_create(self):
        response = self.client.post(reverse('blog_create'), {
            'title': 'test_title',
            'author': self.user,
            'publisher': 'test',
            'lesson': 'persian',
            'grade': 'other',
        })
        self.assertEqual(response.status_code, 302)

    def test_blog_update(self):
        response = self.client.post(reverse('blog_update', args=[self.new_post_active.id]), {
            'title': 'TestTitle',
        })
        self.assertEqual(response.status_code, 302)

    def test_blog_delete(self):
        response = self.client.get(reverse('blog_delete', args=[self.new_post_active.id]))
        self.assertEqual(response.status_code, 302)

    def test_active_post_shown(self):
        response = self.client.get(reverse('blog_list'))
        self.assertContains(response, self.new_post_active.title)

    def test_not_active_post_not_shown(self):
        response = self.client.get(reverse('blog_list'))
        self.assertNotContains(response, self.new_post.title)

    def test_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.new_post_active.id]))
        self.assertContains(response, self.new_post_active.title)

    def test_active_comment_shown(self):
        response = self.client.get(reverse('blog_detail', args=[self.new_post_active.id]))
        self.assertContains(response, self.comment_active.text)

    def test_not_active_comment_not_shown(self):
        response = self.client.get(reverse('blog_detail', args=[self.new_post_active.id]))
        self.assertNotContains(response, self.comment.text)

    def test_comment_create(self):
        response = self.client.post(reverse('blog_detail', args=[self.new_post_active.id]), {
            'user': self.user,
            'text': 'comment2',
            'recommend': True,
        })
        self.assertEqual(response.status_code, 302)

    def test_comment_delete(self):
        response = self.client.get(reverse('comment_delete', args=[self.comment_active.id]))
        self.assertEqual(response.status_code, 302)

#  some errors in not_active_comment_not_shown and comment create
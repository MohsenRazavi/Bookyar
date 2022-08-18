from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Book


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='test-user'
        )
        cls.needed_book_active = Book.objects.create(
            title='test_title1',
            book_official_link='https://google.com',
            need_or_add='need',
            user=cls.user,
            publisher='test',
            lesson='persian',
            grade='other',
            is_active=True,
            year=1400,
        )
        cls.needed_book = Book.objects.create(
            title='test_title2',
            book_official_link='https://google.com',
            need_or_add='need',
            user=cls.user,
            publisher='test',
            lesson='persian',
            grade='other',
            is_active=False,
            year=1400,
        )
        cls.added_book_active = Book.objects.create(
            title='test_title3',
            book_official_link= 'https://google.com',
            need_or_add= 'add',
            user=cls.user,
            publisher='test',
            lesson='persian',
            grade='other',
            is_active=True,
            year=1400,
        )
        cls.added_book = Book.objects.create(
            title='test_title4',
            book_official_link= 'https://google.com',
            need_or_add= 'add',
            user=cls.user,
            publisher='test',
            lesson='persian',
            grade='other',
            is_active=False,
            year=1400,
        )

    def test_urls_name(self):
        response1 = self.client.get(reverse('needed_books'))
        response2 = self.client.get(reverse('added_books'))
        response3 = self.client.get(reverse('book_detail', args=[self.added_book_active.id]))

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_needed_shown_in_needed(self):
        response = self.client.get(reverse('needed_books'))
        self.assertContains(response, self.needed_book_active.title)

    def test_needed_not_shown_in_added(self):
        response = self.client.get(reverse('added_books'))
        self.assertNotContains(response, self.needed_book_active.title)

    def test_added_shown_in_added(self):
        response = self.client.get(reverse('added_books'))
        self.assertContains(response, self.added_book_active.title)

    def test_added_not_shown_in_needed(self):
        response = self.client.get(reverse('needed_books'))
        self.assertNotContains(response, self.added_book_active.title)

    def test_not_active_not_shown(self):
        response1 = self.client.get(reverse('needed_books'))
        response2 = self.client.get(reverse('added_books'))

        self.assertNotContains(response1, self.needed_book.title)
        self.assertNotContains(response2, self.added_book.title)

    def test_book_create(self):
        response = self.client.post(reverse('book_create'), {
            'title':'test_title2',
            'book_official_link':'https://google.com',
            'need_or_add':'need',
            'user':self.user,
            'publisher':'test',
            'lesson':'persian',
            'grade':'other',
            'year' : 1400,
        })
        self.assertEqual(response.status_code, 302)

    def test_book_update(self):
        response = self.client.post(reverse('book_update', args=[self.needed_book_active.id]), {
            'title': 'TestTitle',
        })
        self.assertEqual(response.status_code, 302)

    def test_book_delete(self):
        response = self.client.post(reverse('book_delete', args=[self.added_book_active.id]))
        self.assertEqual(response.status_code, 302)



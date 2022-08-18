from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from books.models import Book
from blog.models import Post


class SignupTests(TestCase):
    def test_signup_url(self):
        response1 = self.client.get(reverse('signup'))
        self.assertEqual(response1.status_code, 200)

        response2 = self.client.get('/accounts/signup/')
        self.assertEqual(response2.status_code, 200)

    def test_signup_form(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            'test_username',
            'test@test.com',
        )

        self.assertEqual(UserModel.objects.all().count(), 1)
        self.assertEqual(UserModel.objects.all()[0].username, user.username)
        self.assertEqual(UserModel.objects.all()[0].email, user.email)


class AccountUrlTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.UserModel = get_user_model()
        cls.user = cls.UserModel.objects.create_user(
            'test_username',
        )

    def test_urls(self):
        response1 = self.client.get(reverse('panel', args=[self.user.id]))
        response2 = self.client.get('accounts/panel_info', args=[self.user.id])
        self.assertEqual(response1, response2)

        response3 = self.client.get(reverse('panel_needed_books', args=[self.user.id]))
        response4 = self.client.get('accounts/panel_needed_books', args=[self.user.id])
        self.assertEqual(response3, response4)

        response5 = self.client.get(reverse('panel_added_books', args=[self.user.id]))
        response6 = self.client.get('accounts/panel_added_books', args=[self.user.id])
        self.assertEqual(response5, response6)

        response7 = self.client.get(reverse('panel_posts', args=[self.user.id]))
        response8 = self.client.get('accounts/panel_posts', args=[self.user.id])
        self.assertEqual(response7, response8)

        response9 = self.client.get(reverse('out_view', args=[self.user.id]))
        response10 = self.client.get('accounts/out_view', args=[self.user.id])
        self.assertEqual(response9, response10)

    def test_account_panel_info(self):
        response = self.client.post(reverse('panel', args=[self.user.id]), {
            'username': 'TestUserName',
            'first_name': 'Bob',
        })

        self.assertEqual(response.status_code, 302)

#        test for panel needed added books and posts ....

from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='ksvkabra@gmail.com', password='testpass123'):
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):

        email = 'keshavkabrasikar@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'keshavkabrasikar@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'testpass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'keshavkabrasikar@gmail.com',
            'testpass123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

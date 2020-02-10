from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        #testing for creating a user with test_create_user_with_email
        email='tesla.newface@gmail.com'
        password='nutansagar'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.password,password)

    def new_user_email_normalised(self):

        email="TESLA.NEWFACE@GMAIL.COM"
        user=get_user_model().objects.create_user(
            email=email,
            password="test"
        )
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_super_user(self):
        """to check the super user"""
        user=get_user_model().objects.create_super_user(
            'tesla.newface@gmail.com',
            'testing'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

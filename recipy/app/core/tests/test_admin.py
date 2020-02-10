from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSite(TestCase):

    def setUp(self):
        self.client=Client()
        self.admin_user=get_user_model().objects.create_super_user(
            email='admin@gmail.com',
            password='1234'
        )
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
            email='tesla.newface@gmail.com',
            password='test',
            name='test name'
        )

    def test_users_listed(self):

        url=reverse('admin:core_user_changelist')
        res=self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        #self.assertEqual(res.status_code,200)

    def test_user_change_page(self):
        """Test that the user edit page works"""

        # url example: /admin/core/user/1
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

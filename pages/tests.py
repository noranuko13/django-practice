from django.shortcuts import resolve_url
from django.test import TestCase


class ViewsTest(TestCase):

    def test_admin(self):
        response = self.client.get(resolve_url('admin:login'))
        self.assertContains(response, 'Log in | Django site admin', html=True)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get(resolve_url('pages:index'))
        self.assertContains(response, 'pages:index', html=True)
        self.assertEqual(response.status_code, 200)

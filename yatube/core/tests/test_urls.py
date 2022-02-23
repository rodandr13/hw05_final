from http import HTTPStatus

from django.test import Client, TestCase
from django.core.cache import cache


class CoreUrlsTesting(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cache.clear()

    def test_server_responds_404_unexisted_page(self):
        response = self.guest_client.get('/unixisted-page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

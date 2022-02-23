from django.test import Client, TestCase
from django.core.cache import cache


class CoreViewsTesting(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cache.clear()

    def test_template_404_unexisted_page(self):
        response = self.guest_client.get('/unixisted-page/')
        expect = 'core/404.html'
        self.assertTemplateUsed(response, expect)

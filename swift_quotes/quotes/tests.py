from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_the_home_page(self):
        found = resolve('/quotes/')
        self.assertEqual(found.func, home_page)
# Create your tests here.

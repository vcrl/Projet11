from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import frontpage

class Test_Urls(SimpleTestCase):
    def test_frontpage(self):
        url = reverse('frontpage')
        self.assertEquals(resolve(url).func, frontpage)
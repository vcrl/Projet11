from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import display_products, display_substitutes, product_details, save_product, delete_product
import re

class Test_Urls(SimpleTestCase):
    def test_substitutes(self):
        url = reverse('substitutes')
        self.assertEquals(resolve(url).func, display_substitutes)
    
    def test_products(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, display_products)
    
    def test_save(self):
        url = r'/products/\d+/save/'
        url_to_test = '/products/55/save/'
        self.assertTrue(re.match(url, url_to_test))
    
    def test_delete(self):
        url = r'/products/\d+/delete/'
        url_to_test = '/products/55/delete/'
        self.assertTrue(re.match(url, url_to_test))
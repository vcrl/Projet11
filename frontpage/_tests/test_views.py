from django.test import TestCase, Client
from django.urls import reverse, resolve
import json

class Test_Views(TestCase):
    def init(self):
        self.client = Client()

    def test_frontpage_get(self):
        response = self.client.get(reverse('frontpage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontpage/index.html')
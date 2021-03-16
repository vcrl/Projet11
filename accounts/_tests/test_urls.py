from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import signup, signout, loginuser, displayprofile

class Test_Urls(SimpleTestCase):
    def test_signup(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)
    
    def test_signout(self):
        url = reverse('signout')
        self.assertEquals(resolve(url).func, signout)
    
    def test_signin(self):
        url = reverse('loginuser')
        self.assertEquals(resolve(url).func, loginuser)
    
    def test_profile(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, displayprofile)
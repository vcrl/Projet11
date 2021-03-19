from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib.auth.models import User
from django.contrib import auth
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_Selenium():
    def testform(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000')
        search = selenium.find_element_by_id('searchinput')
        submit = selenium.find_element_by_id('searchsubmit')
        search.send_keys('coca')
        submit.send_keys(Keys.RETURN)
        assert 'Coca-Cola' in selenium.page_source
        search.send_keys('biscuits')
        submit.send_keys(Keys.RETURN)
        assert 'Biscuits' in selenium.page_source
        search.send_keys('eau')
        submit.send_keys(Keys.RETURN)
        assert 'Eau' in selenium.page_source
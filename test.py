import unittest
from login_page import LoginPage
from selenium import webdriver

class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = 'http://127.0.0.1:5000/auth/login'
        self.username = 'blues'
        self.password = '123456'

    def test_login_mail(self):
        login_page = LoginPage(self.driver,self.url,'Sign In - BluesServer')
        login_page.open()
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        login_page.click_submit()

    def tearDown(self):
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()
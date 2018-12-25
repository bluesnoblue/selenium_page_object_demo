from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    username_loc = (By.ID,'username')
    password_loc = (By.ID,'password')
    submit_loc = (By.ID,'submit')

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()


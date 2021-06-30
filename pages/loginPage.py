import data
from pages.page import BasePageStart
from selenium.webdriver.common.by import By



class LoginPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.USERNAME = (By.ID, "txtUsername")
        self.PASSWORD = (By.ID, "txtPassword")
        self.LOGIN_BUTTON = (By.ID, "btnLogin")
        self.driver.implicitly_wait(3)

    def system_login(self):
        username = self.driver.find_element(*self.USERNAME)
        password = self.driver.find_element(*self.PASSWORD)
        loginButton = self.driver.find_element(*self.LOGIN_BUTTON)
        username.send_keys(data.LoginData.username)
        password.send_keys(data.LoginData.password)
        loginButton.click()



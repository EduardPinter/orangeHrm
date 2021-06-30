import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.loginPage import LoginPage
from pages.mainPage import MainPage
from pages.systemUsers import SystemUsersPage


class CheckoutAssertation(unittest.TestCase):

    def setUp(self):

        self.browserName = input("Enter the browser you want to use -> ")

        if self.browserName == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browserName == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            print("Browser name ==> " + self.browserName)

        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_view_system_users(self):
        loginPage = LoginPage(self.driver)
        loginPage.system_login()
        mainPage = MainPage(self.driver)
        mainPage.click_view_system_users()
        systemUsersPage = SystemUsersPage(self.driver)
        systemUsersPage.count_length_of_table()
        systemUsersPage.print_names()






    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.loginPage import LoginPage
from pages.mainPage import MainPage
from pages.myInfoPage import MyInfoPage


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

    def test_my_info(self):
        loginPage = LoginPage(self.driver)
        loginPage.system_login()
        mainPage = MainPage(self.driver)
        mainPage.click_my_info()
        myInfoPage = MyInfoPage(self.driver)
        print("First name : ")
        myInfoPage.get_value_of_field(myInfoPage.FIRST_NAME)
        print("Middle name : ")
        myInfoPage.get_value_of_field(myInfoPage.MIDDLE_NAME)
        print("Last name : ")
        myInfoPage.get_value_of_field(myInfoPage.LAST_NAME)
        print("Employee Id : ")
        myInfoPage.get_value_of_field(myInfoPage.EMPLOYEE_ID)
        print("Marital Status : ")
        myInfoPage.get_selected(myInfoPage.MARITAL_STATUS)
        print("Birth date : ")
        myInfoPage.get_value_of_field(myInfoPage.BIRTH_DATE)
        print("Gender : ")
        myInfoPage.checked_gender()
        print("Nationality : ")
        myInfoPage.get_selected(myInfoPage.NATIONALITY)
        print("License expiry date : ")
        myInfoPage.get_value_of_field(myInfoPage.LICENSE_EXPIRY_DATE)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
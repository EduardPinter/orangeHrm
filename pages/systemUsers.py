import time
import data
from pages.page import BasePageStart
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemUsersPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.LENGTH_OF_TABLE = (By.CSS_SELECTOR, "#resultTable > tbody > tr")
        self.NAMES = (By.CSS_SELECTOR, "#resultTable > tbody > tr > td:nth-child(2) > a")

    def count_length_of_table(self):

        lengthOfTable = self.driver.find_elements(*self.LENGTH_OF_TABLE)
        counter = 0
        for element in lengthOfTable:
            counter += 1
        print("Number of names in the table on the first page is : " + str(counter))

    def print_names(self):

        names = self.driver.find_elements(*self.NAMES)
        for element in names:
            print(element.text)




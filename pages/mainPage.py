import time

import data
from pages.page import BasePageStart
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.NAV_ADMIN_MODULE = (By.ID, "menu_admin_viewAdminModule")
        self.NAV_USER_MANAG = (By.ID, "menu_admin_UserManagement")
        self.NAV_SYSTEM_USERS = (By.ID, "menu_admin_viewSystemUsers")
        self.NAV_MY_DETAILS = (By.ID, "menu_pim_viewMyDetails")

    def click_view_system_users(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NAV_ADMIN_MODULE))
        adminPanel = self.driver.find_element(*self.NAV_ADMIN_MODULE)
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(self.NAV_USER_MANAG))
        adminUserMan = self.driver.find_element(*self.NAV_USER_MANAG)
        ActionChains(self.driver).move_to_element(adminPanel).perform()
        ActionChains(self.driver).move_to_element(adminUserMan).perform()
        self.driver.find_element(*self.NAV_SYSTEM_USERS).click()

    def click_my_info(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NAV_MY_DETAILS))
        self.driver.find_element(*self.NAV_MY_DETAILS).click()

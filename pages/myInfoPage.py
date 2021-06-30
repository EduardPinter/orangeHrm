from pages.page import BasePageStart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyInfoPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.FIRST_NAME = (By.ID, "personal_txtEmpFirstName")
        self.LAST_NAME = (By.ID, "personal_txtEmpLastName")
        self.MIDDLE_NAME = (By.ID, "personal_txtEmpMiddleName")
        self.EMPLOYEE_ID = (By.ID, "personal_txtEmployeeId")
        self.MARITAL_STATUS = (By.ID, "personal_cmbMarital")
        self.BIRTH_DATE = (By.ID, "personal_DOB")
        self.GENDER_MALE = (By.ID, 'personal_optGender_1')
        self.GENDER_FEMALE = (By.ID, "personal_optGender_2")
        self.NATIONALITY = (By.ID, "personal_cmbNation")
        self.LICENSE_EXPIRY_DATE = (By.ID, "personal_txtLicExpDate")

    def get_value_of_field(self, value):
        element = self.driver.find_element(*value)
        print(element.get_attribute("value"))

    def get_selected(self, value):
        select = Select(self.driver.find_element(*value))
        selected_option = select.first_selected_option
        print(selected_option.text)

    def checked_gender(self):
        male = self.driver.find_element(*self.GENDER_MALE)
        female = self.driver.find_element(*self.GENDER_FEMALE)
        if male.is_selected():
            print(self.driver.find_element(By.XPATH, '//*[@id="frmEmpPersonalDetails"]/fieldset/ol[3]/li[1]/ul/li[1]/label').text)
        elif female.is_selected():
            print(self.driver.find_element(By.XPATH, '//*[@id="frmEmpPersonalDetails"]/fieldset/ol[3]/li[1]/ul/li[2]/label').text)



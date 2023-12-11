import pytest
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href$='/angularpractice/shop']")
    name = (By.XPATH, "//input[@minlength='2']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkBox1 = (By.ID, "exampleCheck1")
    genderBox = (By.ID, "exampleFormControlSelect1")
    employmentStatus = (By.XPATH, "//input[@id='inlineRadio2']")
    dateOfBirth = (By.CSS_SELECTOR, "input[name='bday']")
    submitButton = (By.CSS_SELECTOR, "input[value='Submit']")
    successMessage = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getCountrySearch(self):
        self.driver.find_element(*HomePage.countrySearch).send_keys("uni")
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name).send_keys("Kevin Marx")

    def getEmail(self):
        return self.driver.find_element(*HomePage.email).send_keys("kvmmarx@gmail.com")

    def getPassword(self):
        return self.driver.find_element(*HomePage.password).send_keys("K1234567!")

    def getCheckbox1(self):
        return self.driver.find_element(*HomePage.checkBox1).click()

    def getGenderbox(self):
        return self.driver.find_elements(*HomePage.genderBox)

    def getEmploymentStatus(self):
        return self.driver.find_elements(*HomePage.employmentStatus)

    def getDateOfBirth(self):
        return self.driver.find_element(*HomePage.dateOfBirth).send_keys("01/06/2023")

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton).click()

    def getSuccessMessage(self):
        success = self.driver.find_element(*HomePage.successMessage)
        assert "Success!" in success.text
        return success

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName()
        log.info("Name is entered successfully")

        homePage.getEmail()
        log.info("email is entered successfully")

        homePage.getPassword()
        log.info("password is entered successfully")

        homePage.getCheckbox1()
        log.info("Icecream checkbox clicked successfully")

        gender = homePage.getGenderbox()

        for genders in gender:
            male = genders.find_element(By.XPATH, "//option[normalize-space()='Male']")
            female = genders.find_element(By.XPATH, "//option[normalize-space()='Female']")
            assert male.text == "Male"
            if female.text == "Female":
                female.click()
        log.info("female gender clicked successfully")

        statuses = homePage.getEmploymentStatus()

        for status in statuses:
            status.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()
        log.info("Employed radius clicked successfully")

        homePage.getDateOfBirth()
        log.info("Date of Birth entered successfully")

        homePage.getSubmitButton()
        log.info("Submit tab clicked successfully")

        homePage.getSuccessMessage()
        log.info("Success message is displayed successfully")

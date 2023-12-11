from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    clickCheckout = (By.XPATH, "//div[@id='navbarResponsive']/ul/li/a")
    checkoutTotal = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getClickCheckout(self):
        return self.driver.find_element(*CheckOutPage.clickCheckout).click()

    def getClickCheckoutTotal(self):
        self.driver.find_element(*CheckOutPage.checkoutTotal).click()
        countrySearch = ConfirmPage(self.driver)
        return countrySearch

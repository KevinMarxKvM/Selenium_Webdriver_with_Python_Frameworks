import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass


class TestOne(Baseclass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("click in the first page")

        products = checkoutPage.getCardTitle()  # all the product's name

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "(//button[contains(text(),'Add')])[4]").click()

        log.info("getting all the products name and selecting one of them")

        checkoutPage.getClickCheckout()
        log.info("clicking on checkout tab 1")

        confirmPage = checkoutPage.getClickCheckoutTotal()
        log.info("clicking on checkout Total tab")

        confirmPage.getCountrySearch()
        log.info("looking for the country with 'Uni' text")

        time.sleep(5)

        confirmPage.getCountryConfirm()
        log.info("confirming United Kingdom")

        confirmPage.getClickCheckbox()
        log.info("clicking on the confirmation checkbox")

        confirmPage.getSubmit()
        log.info("clicking on Submit")

        confirmPage.getSuccess()
        log.info("Getting success message")

import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass



#@pytest.mark.usefixtures("setup")
class TestOne(Baseclass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()  #checkoutPage = CheckOutPage(self.driver)
        log.info("click in the first page")

        products = checkoutPage.getCardTitle()    # all the product's name

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "(//button[contains(text(),'Add')])[4]").click()

        log.info("getting all the products name and selecting one of them")

        checkoutPage.getClickCheckout()    #click on the checkout tab #1

        log.info("clicking on checkout tab 1")


        confirmPage = checkoutPage.getClickCheckoutTotal()   #click on the checkout tab #2
        log.info("clicking on checkout Total tab")

        confirmPage.getCountrySearch()
        #self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("uni")  #Country search
        log.info("looking for the country with 'Uni' text")

        time.sleep(5)

        confirmPage.getCountryConfirm()
        log.info("confirming United Kingdom")
        #self.driver.find_element(By.LINK_TEXT, "United Kingdom").click()   #click on country

        confirmPage.getClickCheckbox()
        log.info("clicking on the confirmation checkbox")
        #self.driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()  #click checkbox

        confirmPage.getSubmit()
        log.info("clicking on Submit")
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()  #Sumbit

        confirmPage.getSuccess()
        log.info("Getting success message")
        #success = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
        #assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in success



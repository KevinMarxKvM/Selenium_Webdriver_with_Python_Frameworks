from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countrySearch = (By.XPATH, "//input[@id='country']")
    countryConfirm = (By.LINK_TEXT, "United Kingdom")
    clickCheckbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    def getCountrySearch(self):
        return self.driver.find_element(*ConfirmPage.countrySearch).send_keys("uni")

    def getCountryConfirm(self):
        return self.driver.find_element(*ConfirmPage.countryConfirm).click()

    def getClickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.clickCheckbox).click()

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit).click()

    def getSuccess(self):
        success = self.driver.find_element(*ConfirmPage.success).text
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in success

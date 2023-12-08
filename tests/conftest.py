from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        # options.add_argument("headless")
        # options.add_argument("--ignore-certificate-errors")
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj, options=options)
        driver.implicitly_wait(4)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")

        service_obj = Service()
        driver = webdriver.Edge(service=service_obj, options=options)
        driver.implicitly_wait(4)

    elif browser_name == "IE":
        options = webdriver.IeOptions()
        options.add_additional_option("detach", True)
        options.add_argument("--start-maximized")

        service_obj = Service()
        driver = webdriver.Ie(service=service_obj, options=options)
        driver.implicitly_wait(4)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


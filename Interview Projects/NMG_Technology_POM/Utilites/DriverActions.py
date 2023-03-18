from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DriverAction:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, wait=20, by=By.XPATH):
        element = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((by, locator)))
        return element

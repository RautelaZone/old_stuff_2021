from selenium.webdriver.common.by import By
from POM.Utilites.DriverActions import DriverAction


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.da = DriverAction(self.driver)
        self.usernname_textBox_id = "username"
        self.password_textBox_id = "password"
        self.sign_button_xpath = "//span[contains(text(),' Sign In ')]"

    def enter_user_name(self, username):
        user_name = self.da.wait_for_element(self.usernname_textBox_id, by=By.ID)
        user_name.clear()
        user_name.send_keys(username)

    def enter_password(self, password):
        pwd = self.da.wait_for_element(self.password_textBox_id, by=By.ID)
        pwd.clear()
        pwd.send_keys(password)

    def click_sign_in_button(self):
        self.da.wait_for_element(self.sign_button_xpath).click()

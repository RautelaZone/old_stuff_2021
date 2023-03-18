from selenium.webdriver.common.by import By

from PageObjectModel.Config.config import TestData
from PageObjectModel.Pages.BasePage import BasePage
from PageObjectModel.Pages.HomePage import HomePage


class LoginPage(BasePage):
    """ By Locators/Object Repository """
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    """ Constructors of the page class """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ Page Actions/Methods """

    # Will return page title
    def get_login_page_title(self, title):
        return self.get_login_page_title(title)

    # Will check for the visibility of Signup link
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    # Will login into the application : app.hubspot.com
    def do_login(self, username, password):
        self.do_sendKeys(self.EMAIL,username)
        self.do_sendKeys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
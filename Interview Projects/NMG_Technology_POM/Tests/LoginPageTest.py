import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from POM.Pages.HomePage import HomePage
from POM.Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        time.sleep(5)

    def test_Login(self):
        URL = "https://cs.staging.competiscan.com/"
        user_name = "manas"
        pwd = "Welcome@1234567"

        driver = self.driver
        driver.get(URL)
        print("")
        print("*"*70)
        print("Logged in to the application.")
        login = LoginPage(driver)
        login.enter_user_name(user_name)
        login.enter_password(pwd)
        login.click_sign_in_button()

        """
        Following LOC will perform:
        1) Selecting option 'Unused'
        2) Clicking check-box
        3) Clicking Update button 
        4) Refreshing the page and then
        5) Asserting the selected text
        """
        homepage = HomePage(driver)
        selectedOption = homepage.select_option_and_update()
        assert selectedOption == "Unused"

        """
        Following LOC will perform:
        1) Selecting blank option
        2) Clicking check-box
        3) Clicking Update button 
        4) Refreshing the page and then
        5) Asserting the selected text
        """
        selectedOption = homepage.select_blank_option_and_update()
        assert selectedOption == ""

        """
        Signing out from the application
        """
        homepage.logout()
        print("Logged out from the application.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed.")

from PageObjectModel.Tests.test_Base import BaseTest
from PageObjectModel.Config.config import TestData
from PageObjectModel.Pages.LoginPage import LoginPage

class Test_HomePage(BaseTest):

    def test_verify_homepage_title(self):
        self.loginpage = LoginPage(self.driver)
        homePage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_verify_setting_icon(self):
        self.loginpage = LoginPage(self.driver)
        homePage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homePage.is_settings_icon_exits()



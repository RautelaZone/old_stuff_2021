from PageObjectModel.Config.config import TestData
from PageObjectModel.Pages.LoginPage import LoginPage
from PageObjectModel.Tests.test_Base import BaseTest


class Test_Login(BaseTest):

    def test_verifySignupLink(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_verifyPageTitle(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

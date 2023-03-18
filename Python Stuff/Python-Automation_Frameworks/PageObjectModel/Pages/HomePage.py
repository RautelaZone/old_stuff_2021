from selenium.webdriver.common.by import By
from PageObjectModel.Pages.BasePage import BasePage


class HomePage(BasePage):
    SETTING_ICON = (By.ID, "Layer_1")
    PROFILE_ICON = (By.ID, "account-menu")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_settings_icon_exits(self):
        return self.is_visible(self.SETTING_ICON)

    def get_profile_name(self):
        if self.is_visible(self.PROFILE_ICON):
            return self.get_element_text(self.PROFILE_ICON)


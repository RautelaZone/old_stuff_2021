from selenium.webdriver.common.by import By
from POM.Utilites.DriverActions import DriverAction


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.da = DriverAction(driver)

        self.drop_down_xpath = "//div[contains(text(),'48131421')]//following::div[1]"
        self.option_css = "#app > div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(2)>div>div"
        self.blank_option_xpath = "//div[contains(text(),'48131421')]//following::div[@class='v-list-item__content'][1]"
        self.check_box_xpath = "//div[contains(text(),'48131421')]//preceding::div[@class='v-input--selection-controls__ripple'][1]"
        self.update_button_xpath = "//span[contains(text(),'Update')]"
        self.alert_ok_button_xpath = "//span[contains(text(),'Ok')]"
        self.sign_out_xpath = "//span[contains(text(),'Sign Out')]"

    def select_option_and_update(self):
        self.da.wait_for_element(self.drop_down_xpath).click()
        selectedOption = self.da.wait_for_element(self.option_css, by=By.CSS_SELECTOR)
        selectedText = selectedOption.text
        selectedOption.click()
        self.da.wait_for_element(self.check_box_xpath).click()
        self.da.wait_for_element(self.update_button_xpath).click()
        self.da.wait_for_element(self.alert_ok_button_xpath).click()

        self.driver.refresh()
        return selectedText

    def select_blank_option_and_update(self):
        self.da.wait_for_element(self.drop_down_xpath).click()
        selectedOption = self.da.wait_for_element(self.blank_option_xpath)
        selectedText = selectedOption.text
        selectedOption.click()
        self.da.wait_for_element(self.check_box_xpath).click()
        self.da.wait_for_element(self.update_button_xpath).click()
        self.da.wait_for_element(self.alert_ok_button_xpath).click()
        self.driver.refresh()

        return selectedText

    def logout(self):
        self.da.wait_for_element(self.sign_out_xpath).click()

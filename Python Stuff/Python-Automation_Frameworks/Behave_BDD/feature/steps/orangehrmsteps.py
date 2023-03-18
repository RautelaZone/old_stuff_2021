from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Automation\PyCharmWorkSpace\Drivers\chromedriver.exe")

@when('open orangeHRM home page')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('maximize the window')
def maximizeWindow(context):
    context.driver.maximize_window()

@then('verify the logo present on the page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('close the browser')
def closeBrowser(context):
    context.driver.close()



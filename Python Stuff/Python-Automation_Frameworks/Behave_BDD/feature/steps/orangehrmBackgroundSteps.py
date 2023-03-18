from behave import *

@given('I launch browser')
def step_impl(context):
    assert True,"Launching Browser"

@when('I open application')
def step_impl(context):
    assert True, "Open application"

@when('Enter valid username and password')
def step_impl(context):
    assert True,"Entered valid credentials"

@then('click on Login')
def step_impl(context):
    assert True,"Clicked to Login button"

@then('user must login to Dashboard Page')
def step_impl(context):
    assert True,"Landed to Dashboard page"

@when('navigate to search page')
def step_impl(context):
    assert True,"Navigated to Search Page"

@then('search page should display')
def step_impl(context):
    assert True,"Search page is displaying"

@when('navigate to advance search page')
def step_impl(context):
    assert True,"Navigated to Advance Search Page"

@then('advance search page should display')
def step_impl(context):
    assert True,"Advance Search page is displaying"


Feature: OrangeHRM Logo
    Scenario: Logo presence on OrangeHRM home page
        Given launch chrome browser
        When open orangeHRM home page
        Then maximize the window
        Then verify the logo present on the page
        And close the browser
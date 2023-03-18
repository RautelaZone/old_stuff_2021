Feature: OrangeHRM Login

    Background: common steps
        Given I launch browser
        When I open application
        And Enter valid username and password
        Then click on Login

    Scenario: Login to HRM application
        Then user must login to Dashboard Page

    Scenario: Search User
        When navigate to search page
        Then search page should display

    Scenario: Advance Search User
        When navigate to advance search page
        Then advance search page should display

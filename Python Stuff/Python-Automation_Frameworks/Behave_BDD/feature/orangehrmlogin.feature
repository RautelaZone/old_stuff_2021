Feature: OrangeHRM Login
    Scenario: Login to OrangeHRM with valid credentials
        Given I launch Chrome Browser
        When I open Orange HRM Homepage
        And Enter username "Admin" and password "admin123"
        And Click on Login button
        Then User must successfully login to Dashboard Page

    Scenario Outline: Login to OrangeHRM with multiple credentials
        Given I launch Chrome Browser
        When I open Orange HRM Homepage
        And Enter username "<username>" and password "<password>"
        And Click on Login button
        Then User must successfully login to Dashboard Page

        Examples:
            | username | password |
            | admin    | admin123 |
            | admin123 | admin    |
            | adminxyz | admin123 |
            | admin    | adminxyz |





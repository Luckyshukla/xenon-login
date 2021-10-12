Feature: Xenon Login

  Scenario Outline:  Login to xenon with Multiple parameters
    Given I launch Chrome browser
    When I open xenon login dashboard
    And Enter user name "<username>" and password "<password>"
    And click on login button
    Then User must successfully login to dashboard page

    Examples:
      | username                   | password    |
      | admin                      | admin123    |
      | km.saloni+1@xenonstack.com | Saloni#1999 |
      | admin                      | make123f    |
      | xenon                      | xenon123    |
      | km.saloni+1@xenonstack.com |             |
      |                            | Saloni#1999 |
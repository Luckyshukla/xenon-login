Feature: Forget password
  Scenario: Retract the password passing username
    Given launch Chrome browser
    When open xenon login dashboard
    And click on forget button
    And Enter the username
    And Hit the submit button
    Then User must Retract the password
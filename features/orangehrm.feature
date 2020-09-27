Feature: Test OrangeHRM Application
  Scenario: Validate Login into OrangeHRM
    Given launch browser
    When open orange hrm homepage
    Then verify the logo
    And enter username Admin
    And enter password admin123
    And press login
    And close browser

  Scenario: Apply Leave in OrangeHRM
    Given launch browser
    When open orange hrm homepage
    Then verify the logo
    And enter username Admin
    And enter password admin123
    And press login
    And open leaves tab
    And select leave type as Vacation US
    And apply leave from 2020-09-29
    And apply leave to 2020-09-29
    And apply leave
    And close browser

 Scenario: Search Leave in OrangeHRM
    Given launch browser
    When open orange hrm homepage
    Then verify the logo
    And enter username Admin
    And enter password admin123
    And press login
    And open my leaves tab
    And search leave from 2020-09-29
    And search leave to 2020-09-29
    And search
    And close browser

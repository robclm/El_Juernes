Feature: Login
  In order to access to my personal workspace
  As a user
  I want to log in to the system

  Background: There is a registered user
    Given Exists a user "user" with password "password"


  Scenario: Headcopywriter wants to login to the system
    Given I login as user "user" with password "password"
    Then I'm viewing user "username" workspace

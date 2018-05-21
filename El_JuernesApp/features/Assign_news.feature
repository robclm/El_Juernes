Feature: Assign_news
  as a Head_Copywriter
  I want to assign the AFE news associating a priority
  In order to write an article

  Background: There is a registered user
    Given Exists a HeadCoywriter "HW2" with password "password"
    Given Exists a Coywriter "CW" with password "password"

  Scenario: Headcopywriter wants assign new AFE news
    Given I login a headcopywriter "HW2" with password "password"
    When I assign AFE new
    Then I'm viewing the new assigned in the workload of copywriter
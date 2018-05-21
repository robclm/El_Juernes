Feature: AFE
  as a Head_Copywriter
  I want to receive the news from the AFE
  In order to decide which new to elaborate

  Background: There is a registered user
    Given Exists a HeadCoywriter "HW" with password "password"

  Scenario: Headcopywriter wants visualize new AFE news
    Given I login a headcopywriter "HW" with password "password"
    When I visit the AFE news page
    Then I'm viewing the Afe News List
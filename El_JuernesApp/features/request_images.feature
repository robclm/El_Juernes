Feature: Request_images
  as a Copywriter
  I want to request images for the article
  In order to send an article

  Scenario: Copywriter wants request images for the article
    Given I login as user "CW1" with password "password""
    When I request images
    Then I'm viewing the "Ja s'ha fet la petició Encara no s'ha rebut cap imatge" mesage
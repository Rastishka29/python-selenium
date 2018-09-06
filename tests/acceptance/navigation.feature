Feature: Test navigation between pages

  Scenario: HomePage can go to the BlogPage
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am navigated to the Blog page

  Scenario: BlogPage can go to the HomePage
    Given I am on the Blog page
    When I click on the "Go to home" link
    Then I am navigated to the Home page
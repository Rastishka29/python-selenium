Feature: Test that pages have correct content

  Scenario: Blog page has a correct title
    Given I am on the Blog page
    Then The title shown on the page
    And The title tag has the content "This is the blog page"


  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then The title shown on the page
    And The title tag has the content "This is the homepage"

  Scenario: Blog page loads the posts
    Given I am on the Blog page
    And I wait for the posts to load
    Then I can see that there is a posts section on the page

  Scenario: User can create posts
    Given I am on the new Post Page
    When I enter "Test Post" in the "title" field
    And I enter "Test Content" in the "content" field
    And I press the submit button
    Then I am on the Blog page
    Given I wait for the posts to load
    Then I can see that there is the post with the title "Test Post" in the posts section


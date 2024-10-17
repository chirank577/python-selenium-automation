# Created by chiranjivisingh at 9/18/24
@smoke
Feature: Tests for product page with loops

  Scenario: User can search colors
    Given Open Target product A-91511634 page
    Then Verify user can click through colours

  Scenario: User can search colors
    Given Open Target product A-54551690 pages two
    Then Verify user can click through colours of pants

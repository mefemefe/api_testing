Feature: Trello API Attachments
    As a user
    I want "Attachments" API endpoints
    In order to manipulate attachments

    Scenario: GET all attachments from a card
        Given I created a new card
        And I created an attachment on the card
        When I send a "GET" request to "/cards/{card}/attachments"
        Then I receive a list with at least "1" "attachment"
        And I receive a response with the "get_attachments" schema
        And the status code is "200"

    Scenario: GET an attachment from a card
        Given I created a new card
        And I created an attachment on the card
        When I send a "GET" request to "/cards/{card}/attachments/{attachment}"
        Then I receive a response with the "attachment" schema
        And the status code is "200"

    Scenario Outline: POST an attachment to a card from an url
        Given I created a new card
        When I send a "POST" request to "/cards/{card}/attachments"
            | Key      | Value   |
            | url      | <URL>   |
            | name     | <Name>  |
            | setCover | <Cover> |
        Then the attachment is<bool> created on the card
        And I receive a response with the "attachment" schema
        And the status code is "<Code>"

    Examples:
        | URL                                            | Name          | Cover | bool | Code | comment                             |
        | word                                           | not_a_url     | false |      | 200  | API completes it as "http://word"   |
        | https://www.svgrepo.com/show/354463/trello.svg | Trello logo   | false |      | 200  | normal image attachment             |
        |                                                | empty_url     | false | n't  | 400  | API creates nothing and returns 400 |
        | fpt.aaa.bbb.ccc                                | invalid       | false |      | 200  | API adds "http://" and returns 200  |
        | https://source.unsplash.com/user/c_v_r         | cover         | true  |      | 200  | cover image attachment              |
    
    Scenario: DELETE an attachment from a card
        Given I created a new card
        And I created an attachment on the card
        When I send a "DELETE" request to "/cards/{card}/attachments/{attachment}"
        Then I receive a response with the "delete" schema
        And the status code is "200"
    
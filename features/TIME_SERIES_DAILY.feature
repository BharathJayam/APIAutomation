# Created by bj185044 at 9/21/2021
Feature: To Validate Time Series
  Scenario Outline: Validate by sending  5 requests per Min
    Given Report file is created
    And the required <symbol> provided
    When  User will send <num> requests in one min and validate response
    Then Valid Json Response received
    Examples:
     |symbol|num|
     |IBM|5    |

  Scenario Outline: Validate Response is generated based on symbol
    Given Report file is created
    And the required <function> and <symbol> and <apikey> and provided
    When we execute the Get method
    Then status code of response should be 200
    And Valid Json Response received
    Examples:
     |function| symbol| apikey|
     |TIME_SERIES_DAILY|IBM|Y5YXY8OKSWGERFXC|


  Scenario Outline: Validate output size is Full Size
    Given Report file is created
    And the required <symbol> and <outputsize> provided
    When we execute the Get method
    Then status code of response should be 200
    And Validate response has file has Full size
    And Valid Json Response received
    Examples:
     |outputsize|symbol|
     |full   |IBM|



  Scenario Outline: Validate response data type when datatype is csv
    Given Report file is created
    And the required <symbol> with <datatype> provided
    When we execute the Get method
    Then status code of response should be 200
    And Response Generated in csv format
    Examples:
     |datatype| symbol|
     |csv|IBM|

  Scenario Outline: Validate by sending more than 5 requests per Min
    Given Report file is created
    And the required <symbol> provided
    When  User will send more that 5 requests in a min
    Then  Validate that Error message is shown
    Examples:
     |symbol|
     |IBM|



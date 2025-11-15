*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  user
    Set Password  pswd1234
    Set Confirmation  pswd1234
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  u
    Set Password  pswd1234
    Set Confirmation  pswd1234
    Click Button  Register
    Register Page Should Be Open
    

Register With Valid Username And Too Short Password
    Set Username  user
    Set Password  pswd123
    Set Confirmation  pswd123
    Click Button  Register
    Register Page Should Be Open

Register With Valid Username And Invalid Password
    Set Username  user
    Set Password  pswdpswd
    Set Confirmation  pswdpswd
    Click Button  Register
    Register Page Should Be Open

Register With Nonmatching Password And Password Confirmation
    Set Username  user
    Set Password  pswd1234
    Set Confirmation  pswd2345
    Click Button  Register
    Register Page Should Be Open

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle123
    Click Button  Register
    Register Page Should Be Open


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  name=password_confirmation  ${password_confirmation}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
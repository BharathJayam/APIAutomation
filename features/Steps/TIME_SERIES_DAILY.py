import pytest
import requests
from behave import *
from ratelimit import limits, sleep_and_retry
import json
from CommonFunctions import CommonFunctions
import time


@given("Report file is created")
def step_impl(context):
    CommonFunctions.Create_Report(context.scenario.name)


@given('the required {function} and {symbol} and {apikey} and provided')
def step_impl(context, function, symbol, apikey):
    context.url = 'https://www.alphavantage.co/query'
    context.vparams = {'function': function, 'symbol': symbol, 'apikey': apikey}
    CommonFunctions.fun_Result("Pass", "URL", context.url)
    CommonFunctions.fun_Result("Pass", "params", context.vparams)


@given('the required {symbol} and {outputsize} provided')
def step_impl(context, symbol, outputsize):
    context.url = 'https://www.alphavantage.co/query'
    context.vparams = {'function': 'TIME_SERIES_DAILY', 'symbol': symbol, 'apikey': 'Y5YXY8OKSWGERFXC','outputsize': outputsize}
    context.vSize=outputsize

@given('the required {symbol} with {datatype} provided')
def step_impl(context, symbol, datatype):
    context.url = 'https://www.alphavantage.co/query'
    context.vparams = {'function': 'TIME_SERIES_DAILY', 'symbol': symbol, 'apikey': 'Y5YXY8OKSWGERFXC',
                       'datatype': datatype}


@given('the required {symbol} provided')
def step_impl(context, symbol):
    context.url = 'https://www.alphavantage.co/query'
    context.vparams = {'function': 'TIME_SERIES_DAILY', 'symbol': symbol, 'apikey': 'Y5YXY8OKSWGERFXC'}


@When('we execute the Get method')
@sleep_and_retry
@limits(1, 60)
def Step_imp(context):
    time.sleep(60)
    context.response = requests.get(context.url, params=context.vparams)
    if context.response.status_code != 200:
        raise Exception('API response: {}'.format(context.response.status_code))


@when('User will send {num} requests in one min and validate response')
@sleep_and_retry
@limits(5, 60)
def Step_imp(context, num):
    time.sleep(60)
    for i in range(1,int(num)):
        context.response = requests.get(context.url, params=context.vparams)
        responsejson = json.loads(str((context.response.text)))
        sortedresponseJson = sorted(responsejson.items())
        Expectedresponse = CommonFunctions.JsonFiletoItems("IBM.Json")
        if Expectedresponse == sortedresponseJson:
            CommonFunctions.fun_Result("Pass", Expectedresponse, sortedresponseJson)
        else:
            CommonFunctions.fun_Result("Fail", Expectedresponse, sortedresponseJson)


@when('User will send more that 5 requests in a min')
@sleep_and_retry
@limits(5, 60)
def Step_imp(context):
    time.sleep(60)
    for i in range(7):
        context.response = requests.get(context.url, params=context.vparams)





@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    assert context.response.status_code == statusCode
    CommonFunctions.fun_Result("Pass", "statusCode", context.response.status_code)


@then('Valid Json Response received')
def step_impl(context):
    responsejson = json.loads(str((context.response.text)))
    sortedresponseJson = sorted(responsejson.items())
    if "Full size" in (context.response.text):
        Expectedresponse = CommonFunctions.JsonFiletoItems("IBMfull.Json")
    else:
        Expectedresponse = CommonFunctions.JsonFiletoItems("IBM.Json")
    if Expectedresponse == sortedresponseJson:
        CommonFunctions.fun_Result("Pass", Expectedresponse, sortedresponseJson)
    else:
        CommonFunctions.fun_Result("Fail", Expectedresponse, sortedresponseJson)


@Then("Validate response has file has Full size")
def step_impl(context):
        if ("Full size") in str(context.response.text):
            CommonFunctions.fun_Result("Pass", "Received  response type", "Full size")
        else:
            CommonFunctions.fun_Result("Fail", "Received  response type", "Not Full size")


@Then("Response Generated in csv format")
def step_impl(context):
        if ("Meta Data") in str(context.response.text):
            CommonFunctions.fun_Result("Fail", "Generated File format is", " Not CSV")
        else:
            CommonFunctions.fun_Result("Pass", "Generated File format is", "CSV")


@then("Validate that Error message is shown")
def step_impl(context):
    responsejson = json.loads(str((context.response.text)))
    sortedresponseJson = sorted(responsejson.items())
    if ("Our standard API call frequency is 5 calls per minute and 500 calls per day") in str(context.response.text):
        CommonFunctions.fun_Result("Pass", " Received response as", str(context.response.text))
    else:
        CommonFunctions.fun_Result("Fail", "Our standard API call frequency is 5 calls per minute and 500 calls per day",sortedresponseJson)
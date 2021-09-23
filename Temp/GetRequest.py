#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=Y5YXY8OKSWGERFXC
import json
import time
from CommonFunctions import CommonFunctions
import requests
from ratelimit import limits
url="https://www.alphavantage.co/query"
vparams={'function':'TIME_SERIES_DAILY','symbol':'IBM','apikey':'Y5YXY8OKSWGERFXC','datatype':'csv'}
vMaxCalls=6
vMaxTime=100
@limits(vMaxCalls,vMaxTime)
def call_api(url,vparams):
    Reportfile=CommonFunctions.Create_Report("Get Request")
    print(Reportfile)
    response=requests.get(url,params=vparams)
    responseString=str((response.text))
    Strresponse = str(response.text)
    temp=Strresponse.split(",")
    if temp[0]=="timestamp":
        print("File is csv")

    #for j in range(temp.__sizeof__()):
    #CommonFunctions.fun_Result(Reportfile,"Pass","url is",url)
    #CommonFunctions.fun_Result(Reportfile,"Pass","params is",str(vparams))
    #sortedresponseJson=sorted(responsejson.items())
    #Expectedresponse=CommonFunctions.JsonFiletoItems("IBM.Json")
    #print(Expectedresponse==sortedresponseJson)
    #time.sleep(vMaxTime / vMaxCalls)
    print(response.status_code)
    #CommonFunctions.fun_Result(Reportfile,"Pass","Response code",str(response.status_code))
    #print(response.text)
    #print(type(response))
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
        print("Too many calls")
    return response
for i in range(1):

    print(i)
    print("*******************************************")
    call_api(url,vparams)

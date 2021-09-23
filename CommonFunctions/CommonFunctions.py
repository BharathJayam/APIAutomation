import glob
import json
import os
from ratelimit import limits
import requests
from datetime import datetime

def JsonFiletoItems(symbol):
    with open("RefFile\\"+symbol) as f:
        json1_dict = json.load(f)
    return sorted(json1_dict.items())
def SendRequest(vMaxCalls,vMaxTime,url,vparams):
    @limits(vMaxCalls,vMaxTime)
    def call_api(url,vparams):
        response=requests.get(url,params=vparams)

def Create_Report(TestCaseName):
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    file1 = open("Reports\\ "+ TestCaseName + dt_string + ".txt", "w")
    file1.write('******************************************************** \n')
    file1.write(TestCaseName + "\n")
    file1.write('******************************************************** \n')
    file1.close()

def fun_Result(TestResult,Expected,Actual):
    folder_path = "Reports\\"
    file_type = '\*txt'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    file2 = open(max_file, "a")
    file2.write("\n")
    file2.write("_____"+TestResult+"______"+"\n")
    file2.write("Expected is"+ ":" + str(Expected)+"\n")
    file2.write("Actual:" + str(Actual) + "\n")










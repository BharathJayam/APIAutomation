import glob
import os
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")
TestName="First test case"
path= '../Reports\\'
Filename=path+TestName+dt_string+".txt"
file1 = open(Filename,"w")
file1.write('******************************************************** \n')
file1.write("TestName \n")
file1.write('******************************************************** \n')
file1.close()

folder_path = '../Reports\\'
file_type = '\*txt'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
print("max_file is " +max_file)
file2 = open(max_file,"a")
file2.write("A \n")
file2.write("TestName \n")

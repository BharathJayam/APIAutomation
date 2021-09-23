#Public variables

#'Tscriptname="Test_ASLogin&Sale_Item"
Tdescription = "Verifying the AS Login functionality"
Tprerequest = "Test"
Tprerequest = "Test"
Tprerequest = "Test"
Resultfolder = "C:\Users\Administrator\Desktop\AS_Automation\Results\"
MyFullDate()
MyDate = Date()
'msgbox(MyDate)
if instr(MyDate, "/") > 0:
    sp = "/"
else:
    if(instr(MyDate, "-") > 0):
    sp = "-"

SplitDate = (MyDate, sp)
MyDay = SplitDate(0)
MyMonth = SplitDate(1)
MyYear = SplitDate(2)
MyTime = TIME()
MySplitTime = Split(MyTime, ":")
MyHour = MySplitTime(0)
MyMin = MySplitTime(1)
MySec = MySplitTime(2)
MyFullDate = MyDay + "_" + MyMonth + "_" + MyYear + "_" + MyHour + "_" + MyMin + "_" + MySec
End
Function
'################################################################################
'Name: HTMLHeader
'Author : Bharath Jayam
'Description: write the script name, Pre-Request and description
'Inputs :
'OutPuts :
'############################################################################
Public
function
HTMLHeader(Tscriptname, Tdescription, Tprerequest)
'JSfolder=Resultfolder&"\canvasjs.min.js"
HTMLscriptName = Tscriptname & "_" & MyFullDate()
HtmlImgfolder = Resultfolder & "\IMG\"&HTMLscriptName
HtmlLogFileHeader = Resultfolder & HTMLscriptName & ".html"
sTable = "<!DOCTYPE html><html><style>body {background-color:#e4e8e8}h1{color:black}table, th, td {border: 0.01px solid #006699;background-color:""#eeebe4"" }th {text-align: left;} </style><body onload=""myFunction();myFunction1();""><script type=""text/javascript"">function myFunction1()  {var x = document.getElementById(""t02"").rows.length;var i;var status=0;var status1=0;var status2=0;var tbl = document.getElementById(""t02"");for (i=1;i<x;i++){var val=tbl.rows[i].cells[4].innerHTML;if (val.indexOf(""PASS"")>0 ){ status=status + 1; } else if (val.indexOf(""FAIL"")>0) { status1=status1+1;}else if (val.indexOf(""WARNING"")>0) { status2=status2+1;}}if (status==0) { status=-0;}if (status1==0) { status1=-0;}if (status2==0) { status2=-0;}var chart = new CanvasJS.Chart(""chartContainer"",{title:{text: ""Test Script Status"",fontFamily: ""arial black""},legend: {verticalAlign: ""bottom"",horizontalAlign: ""center""},theme: ""theme1"",  data: [ { type:""pie"",indexLabelFontFamily: ""Garamond"",indexLabelFontSize: 20,indexLabelFontWeight: ""bold"",startAngle:0,indexLabelFontColor: ""MistyRose"",indexLabelLineColor: ""darkgrey"", indexLabelPlacement: ""inside"",toolTipContent: ""{name}: {y}"",showInLegend: true,indexLabel: ""#percent%"",dataPoints: [{  y: status, name: ""PASS"", legendMarkerType: ""triangle""},	{  y: status1, name: ""Fail"", legendMarkerType: ""square""},{  y: status2, name: ""Warning"", legendMarkerType: ""circle""}]}]});chart.render();}</script><script type=""text/javascript""  src=""canvasjs.min.js""></script><script>function myFunction() { var x = document.getElementById(""t02"").rows.length;document.getElementById(""demo1"").innerHTML =  x-1 ;var i;var status=0;var status1=0;var status2=0;var tbl = document.getElementById(""t02"");for (i=1;i<x;i++){var val=tbl.rows[i].cells[4].innerHTML;if (val.indexOf(""PASS"")>0 ) { status=status + 1; } else if (val.indexOf(""FAIL"")>0) { status1=status1+1;} else if (val.indexOf(""WARNING"")>0) { status2=status2+1;}}document.getElementById(""demo2"").innerHTML = status;document.getElementById(""demo3"").innerHTML = status1;document.getElementById(""demo4"").innerHTML = status2;}</script><h1 style=""text-align:center"">AS Automation Test Report</h1><br><div id=""chartContainer"" style=""height: 300px; width: 100%;""></div><br><table style=""width:100%"" bgcolor=""#e4e8e8""><tr><th width=""20%"">Test Script Name</th><td colspan=""3"">" & Tscriptname & "</td></tr><tr><th>Test Script Description</th><td colspan=""3"">" & Tdescription & "</td></tr><tr><th>Test Script Pre-request</th><td colspan=""3"">" & Tprerequest & "</td></tr><tr><th rowspan=""4"">Execution start Time:</th><td width=""25%"">" & Now() & "</td><td width=""25%""><b>Execution End Time:</b></td><td>Execution End Time_start</td></tr></table><br><table style=""width:100%"" id=""t01"" bgcolor=""#F5F5F5""><tr><th width=""20%"">ToTal Num of Test Steps</th><td id=""demo1"">click on the ActiveX control for to view the status</td></tr><tr><th width=""20%"">Num of Test Steps Pass</th><td id=""demo2"">click on the ActiveX control for to view the status</td></tr><tr><th>Num of Test Steps Fail</th><td id=""demo3"">click on the ActiveX control for to view the status</td></tr><tr><th>Num of Warnings</th><td id=""demo4"">click on the ActiveX control for to view the status</td></tr></table><br><table id=""t02"" bgcolor=""#F5F5F5""></tr><th width=""5%"">StepNumber</th><th width=""30%"">Action</th><th width=""30%"">Expected Result</th><th width=""30%"">Actual Result</th><th width=""5%"">Status</th></tr>"
Set
fso = CreateObject("Scripting.FileSystemObject")
fso.CreateTextFile(HtmlLogFileHeader)
fso.CreateFolder(HtmlImgfolder)
Set
f = fso.GetFile(HtmlLogFileHeader)
Set
fts = f.OpenAsTextStream(8, -2)
fts.WriteLine
sTable
fts.Close
End
Function

'################################################################################
'Name: CaptureScreen
'Author : Bharath Jayam
'Description: To CaptureScreen
'Inputs : Browser Name
'OutPuts :
'######################################################################
Public
Function
CaptureScreen(Browser_Name)
Imglocation = "IMG\"&HTMLscriptName&"\"&Tscriptname&"
_
"&MyFullDate()&".png
"
ImgPath = Resultfolder & Imglocation
If
Browser("name:=.*" & Browser_Name & ".*").Exist
Then
Browser("name:=.*" & Browser_Name & ".*").CaptureBitmap
ImgPath
Else
Desktop.CaptureBitmap
ImgPath
End
If
CaptureScreen = Imglocation
End
Function
'################################################################################
'Name: ChangeEXEEndTime()
'Author : Bharath Jayam
'Description: To change the End execution Time
'Inputs :
'OutPuts :
'######################################################################
Public
Function
ChangeEXEEndTime()

Const
ForReading = 1
Const
ForWriting = 2

Set
objFSO = CreateObject("Scripting.FileSystemObject")
Set
objFile = objFSO.OpenTextFile(HtmlLogFileHeader, ForReading)

strText = objFile.ReadAll
objFile.Close
If
st_Endtime = 1
Then
st_Endtime = now()
strNewText = Replace(strText, "Execution End Time_start", st_Endtime)
else
lst_Endtime = now()
strNewText = Replace(strText, st_Endtime, lst_Endtime)
st_Endtime = lst_Endtime
End
If

Set
objFile = objFSO.OpenTextFile(HtmlLogFileHeader, ForWriting)
objFile.WriteLine
strNewText

objFile.Close
End
Function
'################################################################################
'Name: ReportLog
'Author : Bharath Jayam
'Description: To write log in log file
'Inputs : stepResult,stepSummary,stepDesc
'OutPuts :
'#################################################################################
Public
Function
ReportLog(stepResult, stepSummary, stepDesc, stepactual, Browser_Name)
stepnum = stepnum + 1
stepResult = ucase(stepResult)
If
Instr(1, stepResult, "PASS")
Then
vPasscount = vPasscount + 1
color = "#000000"
sCompStr = "<tr><td color=""B8860B""> step " & stepnum & "</td><td>" & stepSummary & "</td><td>" & stepDesc & "</td><td>" & stepactual & "</td><td bgcolor=""green""><font color=" & color & ">" & stepResult & "</font></td></tr>"
else if Instr(1, stepResult, "FAIL") Then
vFailcount = vFailcount + 1
color = "#000000"
'refImage="C:\LPFramework\Results\IMG\Hydrangeas.png"
refImage = CaptureScreen(Browser_Name)
sCompStr = "<tr><td color=""B8860B""> step " & stepnum & "</td><td>" & stepSummary & "</td><td>" & stepDesc & "</td><td>" & stepactual & "</td><td bgcolor=""red""><font color=" & color & "><a href=""" & refImage & """ target=""_blank"">"&stepResult&"</a></font></td></tr>"
	else if Instr(1,stepResult,"WARNING") Then 
		color="#000000" 
		sCompStr ="<tr><td color=""B8860B""> step "&stepnum&"</td><td>"&stepSummary&"</td><td>"&stepDesc&"</td><td>"&stepactual&"</td><td bgcolor=""gold""><font color="&color&">"&stepResult&"</font></td></tr>"
	End If
	End If
	End If 
	Set fso = CreateObject("Scripting.FileSystemObject") 	
	If (fso.FileExists(HtmlLogFileHeader)) Then 
		Set f = fso.GetFile(HtmlLogFileHeader) 
		Set fts = f.OpenAsTextStream( 8, -2) 
		fts.WriteLine sCompStr 
		fts.Close
		ChangeEXEEndTime()
	Else 
		HTMLHeader Tscriptname,Tdescription,Tprerequest 
		'wait 2	
		st_Endtime=1
		Set f = fso.GetFile(HtmlLogFileHeader) 
		Set fts = f.OpenAsTextStream( 8, -2) 
		fts.WriteLine sCompStr
		fts.Close
		ChangeEXEEndTime()
	End If 
End Function

'################################################################################
'Name: HTMLHeader 
'Description: write the script name, Pre-Request and description
'Inputs : 
'OutPuts : 
'############################################################################ 
Public function SummaryHeader
	'JSfolder=Resultfolder&"\canvasjs.min.js"
	vReportName="AS_SummaryReport_"&MyFullDate()
	'HtmlImgfolder1=Resultfolder&"IMG\"&HTMLscriptName
	VReportpath=Resultfolder&vReportName&".html"
	sTable="<!DOCTYPE html><html><style>body {background-color:#e4e8e8}h1{color:black}table, th, td {border: 0.01px solid #006699;background-color:""B8860B"" }th {text-align: left;} </style><body onload=""myFunction();myFunction1();""><script type=""text/javascript"">function myFunction1()  {var x = document.getElementById(""t02"").rows.length;var i;var status=0;var status1=0;var status2=0;var tbl = document.getElementById(""t02"");for (i=1;i<x;i++){var val=tbl.rows[i].cells[4].innerHTML;if (val.indexOf(""PASS"")>0 ){ status=status + 1; } else if (val.indexOf(""FAIL"")>0) { status1=status1+1;}else if (val.indexOf(""WARNING"")>0) { status2=status2+1;}}if (status==0) { status=-0;}if (status1==0) { status1=-0;}if (status2==0) { status2=-0;}var chart = new CanvasJS.Chart(""chartContainer"",{title:{text: ""Test Script Status"",fontFamily: ""arial black""},legend: {verticalAlign: ""bottom"",horizontalAlign: ""center""},theme: ""theme1"",  data: [ { type:""pie"",indexLabelFontFamily: ""Garamond"",indexLabelFontSize: 20,indexLabelFontWeight: ""bold"",startAngle:0,indexLabelFontColor: ""MistyRose"",indexLabelLineColor: ""darkgrey"", indexLabelPlacement: ""inside"",toolTipContent: ""{name}: {y}"",showInLegend: true,indexLabel: ""#percent%"",dataPoints: [{  y: status, name: ""Number of test cases Pass"", legendMarkerType: ""triangle""},	{  y: status1, name: ""Number of test cases Fail"", legendMarkerType: ""square""},{  y: status2, name: ""Number of Warnings"", legendMarkerType: ""circle""}]}]});chart.render();}</script><script type=""text/javascript""  src=""canvasjs.min.js""></script><script>function myFunction() { var x = document.getElementById(""t02"").rows.length;document.getElementById(""demo1"").innerHTML =  x-1 ;var i;var status=0;var status1=0;var status2=0;var tbl = document.getElementById(""t02"");for (i=1;i<x;i++){var val=tbl.rows[i].cells[4].innerHTML;if (val.indexOf(""PASS"")>0 ) { status=status + 1; } else if (val.indexOf(""FAIL"")>0) { status1=status1+1;} else if (val.indexOf(""WARNING"")>0) { status2=status2+1;}}document.getElementById(""demo2"").innerHTML = status;document.getElementById(""demo3"").innerHTML = status1;document.getElementById(""demo4"").innerHTML = status2;}</script><h1 style=""text-align:center"">Automation Summary Report</h1><br><div id=""chartContainer"" style=""height: 300px; width: 100%;""></div><br><table style=""width:100%"" id=""t01"" bgcolor=""#F5F5F5""><tr><th width=""20%"">ToTal Num of Test Scripts</th><td id=""demo1"">click on the ActiveX control for to view the status</td></tr><tr><th width=""20%"">Num of Test scripts Pass</th><td id=""demo2"">click on the ActiveX control for to view the status</td></tr><tr><th>Num of Test scripts Fail</th><td id=""demo3"">click on the ActiveX control for to view the status</td></tr><tr><th>Num of Warnings</th><td id=""demo4"">click on the ActiveX control for to view the status</td></tr></table><br><table id=""t02"" bgcolor=""#F5F5F5""></tr><th width=""5%"">TS Number</th><th width=""30%"">Test script Name</th><th width=""30%"">TEST script start time</th><th width=""30%"">Test script end time</th><th width=""5%"">Status</th></tr>"
		Set fso = CreateObject("Scripting.FileSystemObject") 
	fso.CreateTextFile(VReportpath) 
	'fso.CreateFolder(HtmlImgfolder)
	Set f = fso.GetFile(VReportpath) 
	Set fts = f.OpenAsTextStream( 8, -2) 
	fts.WriteLine sTable 
	fts.Close
End Function


'################################################################################
'Name: ReportLog 
'Description: To write log in log file 
'Inputs : stepResult,stepSummary,stepDesc 
'OutPuts : 
'################################################################################# 
Public Function SummaryLog(vResult) 

	stepResult1=ucase(vResult)
	vCaseCount=vCaseCount+1
	If Instr(1,stepResult1,"PASS") Then 
		color="#006400" 
		sCompStr ="<tr><td color=""#006400""> Case :"&vCaseCount&"</td><td>"&Tscriptname&"</td><td>"&TSstart&"</td><td>"&now()&"</td><td bgcolor=""white""><font color="&color&"><a href=""" & HtmlLogFileHeader & """ target=""_blank"">"&stepResult1&"</a></font></td></tr>"
	elseif Instr(1,stepResult1,"FAIL") Then 
		color="#8B0000" 		
		sCompStr ="<tr><td color=""#8B0000""> Case :"&vCaseCount&"</td><td>"&Tscriptname&"</td><td>"&TSstart&"</td><td>"&now()&"</td><td bgcolor=""white""><font color="&color&"><a href=""" & HtmlLogFileHeader & """ target=""_blank"">"&stepResult1&"</a></font></td></tr>"
	End If

	Set fso = CreateObject("Scripting.FileSystemObject") 	
	If (fso.FileExists(VReportpath)) Then 
		Set f = fso.GetFile(VReportpath) 
		Set fts = f.OpenAsTextStream( 8, -2) 
		fts.WriteLine sCompStr 
		fts.Close
		'ChangeEXEEndTime()
	Else 
		SummaryHeader
		'wait 2	
		st_Endtime=1
		Set f = fso.GetFile(VReportpath)
		Set fts = f.OpenAsTextStream( 8, -2) 
		fts.WriteLine sCompStr
		fts.Close
		'ChangeEXEEndTime()			
	End If 
End Function






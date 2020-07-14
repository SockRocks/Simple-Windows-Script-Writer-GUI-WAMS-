'Put in the same directory as file_maker.exe. Starts out in the runners folder.'
Set oWS = WScript.CreateObject("WScript.Shell")
userProfile = oWS.ExpandEnvironmentStrings( "%userprofile%" )
dim path 
path = userProfile & "\WAMS\file_maker.exe"
CreateObject("WScript.Shell").Run path
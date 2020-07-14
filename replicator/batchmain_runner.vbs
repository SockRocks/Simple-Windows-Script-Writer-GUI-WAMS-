'Put this in the samples folder'
Dim FSO
Set fso = CreateObject("Scripting.FileSystemObject")
GetCurrentFolder= FSO.GetAbsolutePathName(".")
Dim path
path = GetCurrentFolder & "\batchmain.exe"
Wscript.echo(path)
CreateObject("WScript.Shell").Run path